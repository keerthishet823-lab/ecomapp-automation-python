from dataclasses import dataclass
from typing import Literal

WaitUntil = Literal["load", "domcontentloaded", "networkidle", "commit"]


@dataclass(frozen=True)
class NavigationOptions:
    wait_until: WaitUntil | None = None
    timeout: float | None = None


@dataclass(frozen=True)
class ScreenshotOptions:
    full_page: bool = False
    path: str | None = None


@dataclass(frozen=True)
class SelectOption:
    label: str | None = None
    value: str | None = None
    index: int | None = None
