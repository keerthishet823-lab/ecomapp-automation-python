from dataclasses import dataclass, field
from typing import Literal

Environment = Literal["local", "dev", "qa", "stage", "prod"]


@dataclass(frozen=True)
class Credentials:
    admin_email: str = ""
    # Kept out of repr so it can't leak into failure output or reports.
    admin_password: str = field(default="", repr=False)


@dataclass(frozen=True, kw_only=True)
class EnvironmentConfig:
    """Settings for one environment. Timeouts are in milliseconds."""

    env: Environment
    base_url: str
    api_base_url: str
    default_timeout: int
    navigation_timeout: int
    retries: int
    workers: int
    credentials: Credentials = field(default_factory=Credentials)
