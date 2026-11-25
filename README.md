# ecomapp-automation-python

Playwright + Python (pytest) automation framework for the ecommerce application.
It is the Python counterpart of
[ecomapp-automation](https://github.com/keerthishet823-lab/ecomapp-automation)
(Playwright + TypeScript) and follows the same structure.

## Setup

Requires Python 3.12+.

```
python -m venv .venv
.venv\Scripts\activate            # Windows (macOS/Linux: source .venv/bin/activate)
pip install -e ".[dev]"
playwright install chromium
copy .env.example .env            # macOS/Linux: cp
```

`TEST_ENV` selects the environment: `local` (default), `dev`, `qa`, `stage` or
`prod`. `.env.example` selects `prod`, so tests run against the live site.

## Running tests

| Task | Command |
| --- | --- |
| Everything | `pytest` |
| Smoke / regression | `pytest -m smoke` / `pytest -m regression` |
| Headed, one worker | `pytest --headed -n 0` |
| Debug with the inspector | `PWDEBUG=1 pytest -n 0 -k <name>` (PowerShell: `$env:PWDEBUG=1` first) |
| Another browser | `pytest --browser firefox` (after `playwright install firefox`) |
| Open a trace | `playwright show-trace test-results/<test>/trace.zip` |
| Lint, format, types | `ruff check .`, `ruff format .`, `mypy` |

Workers, retries and timeouts come from the selected environment's config;
`-n` and `--reruns` override the first two. The HTML report is written to
`playwright-report/index.html`; screenshots, videos and traces of failed tests
go to `test-results/`.

## Structure

```
conftest.py                 loads .env, applies workers/retries, registers fixtures
src/ecomapp/
  config/                   EnvironmentManager and one module per environment
  constants/                routes, API endpoints, categories, timeouts
  types/                    shared dataclasses and literals
  utils/                    cross-page helpers
  pages/                    page objects (base/ holds BasePage)
  components/               UI components (base/ holds BaseComponent)
  fixtures/                 pytest fixtures: base, auth, shop
  mocks/                    network mocks
tests/                      test modules
```

## Adding a page

1. Create `src/ecomapp/pages/<name>_page.py` with a class extending `BasePage`.
   Implement `url` using `Routes`, and define locators in `__init__`.
2. Add a fixture for it in `fixtures/shop_fixture.py` (or `auth_fixture.py`).
3. Add `tests/test_<name>.py` and tag tests with `smoke` or `regression`.

## Porting checklist

| TypeScript page | Components it needs | TypeScript spec | Ported |
| --- | --- | --- | --- |
| HomePage | Header, Footer, ProductCard | home-page | ☐ |
| CategoryPage | Header, Footer, ProductCard | category-navigation | ☐ |
| ProductPage | Header, Footer | product-page | ☐ |
| CartPage | Header, Footer | cart | ☐ |
| WishlistPage | Header, Footer | wishlist | ☐ |
| CheckoutPage | — | checkout | ☐ |
| LoginPage | — (Google auth mock) | auth-google-login | ☐ |
| RegisterPage | — | none yet | ☐ |
| AccountPage | ProfileCard, Wishlist, Cart and Orders sections | account-page (commented out) | ☐ |

Signed-in tests are blocked on prod: muvake.com only offers Google OAuth, so the
TypeScript API-login shortcut does not produce a session. They need a non-prod
environment with a credentials provider, or a saved `storage_state` from a real
test account.
