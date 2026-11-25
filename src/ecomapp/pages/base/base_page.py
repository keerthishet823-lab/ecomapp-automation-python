import re
from abc import ABC, abstractmethod

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from ecomapp.types.config_types import EnvironmentConfig
from ecomapp.types.ui_types import NavigationOptions

_GOOGLE_SIGN_IN = re.compile(r"accounts\.google\.com")


class BasePage(ABC):
    def __init__(self, page: Page, config: EnvironmentConfig) -> None:
        self.page = page
        self.config = config

    @property
    @abstractmethod
    def url(self) -> str:
        """Path of this page, relative to the environment's base URL."""

    def goto(self) -> None:
        self.page.goto(self.url)
        self._wait_for_page_load()

    def _navigate(self, path: str, options: NavigationOptions | None = None) -> None:
        options = options or NavigationOptions()
        self.page.goto(path, wait_until=options.wait_until, timeout=options.timeout)

    def _wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")

    def scroll_to_bottom(self, timeout_ms: int = 20_000) -> None:
        """Scroll down in steps until the scroll height stabilizes or time runs out.

        Confirms long or infinite-scroll listings don't hang partway down.
        """
        self.page.evaluate(
            """async (timeout) => {
                const start = Date.now();
                let lastHeight = -1;
                let stableRounds = 0;
                while (Date.now() - start < timeout) {
                    window.scrollTo(0, document.body.scrollHeight);
                    await new Promise((resolve) => setTimeout(resolve, 300));
                    const height = document.body.scrollHeight;
                    if (height === lastHeight) {
                        stableRounds += 1;
                        if (stableRounds >= 2) break;
                    } else {
                        stableRounds = 0;
                    }
                    lastHeight = height;
                }
            }""",
            timeout_ms,
        )

    def wait_for_google_sign_in(self, timeout_ms: int = 30_000) -> bool:
        """Wait for the hand-off to Google's OAuth screen.

        Several guest actions redirect there client-side, after
        ``domcontentloaded``, so reading the URL straight after the action races
        the redirect. Returns False rather than raising so callers can assert on
        the outcome.
        """
        if self.is_at_google_sign_in():
            return True
        try:
            self.page.wait_for_url(_GOOGLE_SIGN_IN, timeout=timeout_ms)
        except PlaywrightTimeoutError:
            return False
        return True

    def is_at_google_sign_in(self) -> bool:
        return "accounts.google.com" in self.page.url

    def is_page_responsive(self) -> bool:
        """A hung page won't evaluate trivial script in a timely manner."""
        try:
            # Unlike evaluate(), wait_for_function() honours a timeout.
            self.page.wait_for_function("() => 1 + 1 === 2", timeout=5_000)
        except PlaywrightTimeoutError:
            return False
        return True
