from playwright.sync_api import Locator, Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


def click_nav_link(page: Page, link: Locator) -> None:
    """Click a Next.js client-side link and confirm the route changed.

    The app's links are server-rendered before their handlers are attached, so
    a click that lands mid-hydration is silently swallowed and the page simply
    stays put. Retrying once against the link's own href makes the navigation
    deterministic without papering over a genuinely broken link: if the second
    click doesn't move either, this raises.
    """
    href = link.get_attribute("href")
    link.click()

    if not href:
        return

    target = f"**{href}"
    try:
        page.wait_for_url(target, timeout=5_000)
    except PlaywrightTimeoutError:
        link.click()
        page.wait_for_url(target, timeout=10_000)
