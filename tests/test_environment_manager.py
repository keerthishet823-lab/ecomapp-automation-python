from collections.abc import Iterator

import pytest

from ecomapp.config import EnvironmentManager


@pytest.fixture(autouse=True)
def _clean_environment() -> Iterator[None]:
    # Owns its MonkeyPatch so variables are restored before the cache is reset.
    with pytest.MonkeyPatch.context() as patch:
        for variable in ("TEST_ENV", "BASE_URL", "API_BASE_URL"):
            patch.delenv(variable, raising=False)
        EnvironmentManager.reset()
        yield
    EnvironmentManager.reset()


def test_defaults_to_local() -> None:
    assert EnvironmentManager.get_config().env == "local"


@pytest.mark.parametrize("env", ["local", "dev", "qa", "stage", "prod"])
def test_selects_the_environment_named_by_test_env(monkeypatch: pytest.MonkeyPatch, env: str) -> None:
    monkeypatch.setenv("TEST_ENV", env)
    assert EnvironmentManager.get_config().env == env


def test_rejects_an_unknown_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TEST_ENV", "nope")
    with pytest.raises(ValueError, match="Invalid TEST_ENV"):
        EnvironmentManager.get_config()


def test_base_url_can_be_overridden(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BASE_URL", "https://preview.example.com")
    assert EnvironmentManager.get_config().base_url == "https://preview.example.com"


def test_rejects_a_base_url_without_a_scheme(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BASE_URL", "muvake.com")
    with pytest.raises(ValueError, match="BASE_URL must include"):
        EnvironmentManager.get_config()
