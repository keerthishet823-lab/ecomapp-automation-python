from playwright.sync_api import Locator, Page


class BaseComponent:
    def __init__(self, page: Page, root: Locator) -> None:
        self.page = page
        self.root = root

    def is_visible(self) -> bool:
        return self.root.is_visible()

    def wait_for_visible(self, timeout: float | None = None) -> None:
        self.root.wait_for(state="visible", timeout=timeout)
