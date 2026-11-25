import os
from dataclasses import replace
from functools import cache

from ecomapp.config.environments import dev, local, prod, qa, stage
from ecomapp.types.config_types import Credentials, EnvironmentConfig

ENV_CONFIGS: dict[str, EnvironmentConfig] = {
    "local": local.config,
    "dev": dev.config,
    "qa": qa.config,
    "stage": stage.config,
    "prod": prod.config,
}


def _url_override(variable: str, default: str) -> str:
    """Resolve a URL override, treating blank as unset.

    A scheme-less value (e.g. ``muvake.com``) would make every relative
    ``goto`` fail with an opaque error, so reject it up front.
    """
    value = os.environ.get(variable, "").strip()
    if not value:
        return default
    if not value.startswith(("http://", "https://")):
        raise ValueError(f'{variable} must include http:// or https://, got "{value}"')
    return value


@cache
def _load_config() -> EnvironmentConfig:
    env = os.environ.get("TEST_ENV", "").strip() or "local"
    static_config = ENV_CONFIGS.get(env)
    if static_config is None:
        raise ValueError(f'Invalid TEST_ENV: "{env}". Valid values: {", ".join(ENV_CONFIGS)}')

    return replace(
        static_config,
        base_url=_url_override("BASE_URL", static_config.base_url),
        api_base_url=_url_override("API_BASE_URL", static_config.api_base_url),
        credentials=Credentials(
            admin_email=os.environ.get("ADMIN_EMAIL", ""),
            admin_password=os.environ.get("ADMIN_PASSWORD", ""),
        ),
    )


class EnvironmentManager:
    """Resolves the active environment from ``TEST_ENV`` plus any overrides."""

    @staticmethod
    def get_config() -> EnvironmentConfig:
        return _load_config()

    @staticmethod
    def reset() -> None:
        """Forget the cached config so the next call re-reads the environment."""
        _load_config.cache_clear()
