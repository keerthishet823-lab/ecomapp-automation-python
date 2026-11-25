from ecomapp.types.config_types import EnvironmentConfig

config = EnvironmentConfig(
    env="prod",
    base_url="https://muvake.com",
    api_base_url="https://api.muvake.com",
    default_timeout=45_000,
    navigation_timeout=60_000,
    retries=2,
    workers=2,
)
