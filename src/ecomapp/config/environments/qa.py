from ecomapp.types.config_types import EnvironmentConfig

config = EnvironmentConfig(
    env="qa",
    base_url="https://qa.ecomapp.example.com",
    api_base_url="https://api.qa.ecomapp.example.com",
    default_timeout=30_000,
    navigation_timeout=45_000,
    retries=1,
    workers=4,
)
