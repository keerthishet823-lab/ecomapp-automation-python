"""Environment-driven setup shared by every test."""

from typing import Any

import pytest
from playwright.sync_api import BrowserContext, Playwright

from ecomapp.config import EnvironmentManager
from ecomapp.types.config_types import EnvironmentConfig

# Default device per browser, so a Firefox run doesn't send Chrome's user agent.
_DESKTOP_DEVICES = {
    "chromium": "Desktop Chrome",
    "firefox": "Desktop Firefox",
    "webkit": "Desktop Safari",
}


@pytest.fixture(scope="session")
def env_config() -> EnvironmentConfig:
    return EnvironmentManager.get_config()


@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args: dict[str, Any],
    playwright: Playwright,
    browser_name: str,
    device: str | None,
) -> dict[str, Any]:
    if device:
        return browser_context_args
    return {**playwright.devices[_DESKTOP_DEVICES[browser_name]], **browser_context_args}


@pytest.fixture
def context(context: BrowserContext, env_config: EnvironmentConfig) -> BrowserContext:
    context.set_default_timeout(env_config.default_timeout)
    context.set_default_navigation_timeout(env_config.navigation_timeout)
    return context
