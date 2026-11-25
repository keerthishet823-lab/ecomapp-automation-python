from ecomapp.types.config_types import EnvironmentConfig

config = EnvironmentConfig(
    env="dev",
    base_url="https://dev.ecomapp.example.com",
    api_base_url="https://api.dev.ecomapp.example.com",
    default_timeout=30_000,
    navigation_timeout=45_000,
    retries=1,
    workers=4,
)
