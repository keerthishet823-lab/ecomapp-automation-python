from dataclasses import dataclass, field


@dataclass(frozen=True)
class GoogleProfile:
    sub: str
    name: str
    email: str
    picture: str


@dataclass(frozen=True)
class AuthSession:
    user: GoogleProfile
    access_token: str = field(repr=False)
