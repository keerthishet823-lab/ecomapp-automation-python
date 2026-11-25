"""Proves the framework wiring end to end. No page objects involved."""

import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_base_url_is_reachable(page: Page, base_url: str) -> None:
    response = page.goto("/")

    assert response is not None
    assert response.ok, f"{base_url} answered {response.status}"
    expect(page).to_have_title(re.compile(r"\S"))
