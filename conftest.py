from dotenv import load_dotenv

# Must run before EnvironmentManager reads os.environ. Real environment
# variables (e.g. in CI) take precedence over .env.
load_dotenv()

import pytest  # noqa: E402

from ecomapp.config import EnvironmentManager  # noqa: E402

pytest_plugins = [
    "ecomapp.fixtures.base_fixture",
    "ecomapp.fixtures.auth_fixture",
    "ecomapp.fixtures.shop_fixture",
]


@pytest.hookimpl(tryfirst=True)
def pytest_xdist_auto_num_workers() -> int:
    """``-n auto`` (the default) means "this environment's worker count"."""
    return EnvironmentManager.get_config().workers


def pytest_configure(config: pytest.Config) -> None:
    """Apply the environment's base URL and retries unless passed as options.

    The base URL is set as an option because a plugin fixture here cannot
    reliably override the ``base_url`` fixture other plugins provide.
    """
    env = EnvironmentManager.get_config()
    if not config.option.base_url:
        config.option.base_url = env.base_url
    if config.option.reruns is None:
        config.option.reruns = env.retries


def pytest_report_header(config: pytest.Config) -> str:
    env = EnvironmentManager.get_config()
    return f"environment: {env.env} ({config.option.base_url}), retries: {config.option.reruns}"
