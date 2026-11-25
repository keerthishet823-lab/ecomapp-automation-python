from ecomapp.types.config_types import EnvironmentConfig

config = EnvironmentConfig(
    env="stage",
    base_url="https://stage.ecomapp.example.com",
    api_base_url="https://api.stage.ecomapp.example.com",
    default_timeout=30_000,
    navigation_timeout=45_000,
    retries=2,
    workers=2,
)
