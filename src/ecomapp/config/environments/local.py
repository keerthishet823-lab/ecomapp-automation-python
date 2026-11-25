from ecomapp.types.config_types import EnvironmentConfig

config = EnvironmentConfig(
    env="local",
    base_url="http://localhost:3000",
    api_base_url="http://localhost:8000",
    default_timeout=30_000,
    navigation_timeout=30_000,
    retries=0,
    workers=4,
)
