# UI Automation: SauceDemo (Playwright + pytest)

Automated UI tests for [saucedemo.com](https://www.saucedemo.com), a public e-commerce practice site.

## What is covered
- **Login:** valid login, and invalid cases (wrong password, unknown user, locked-out user, empty fields)
- **Cart:** adding and removing items, badge count, cart contents
- **Sorting:** price low-to-high and name Z-to-A

## Tech stack
- Python 3.10+
- Playwright for browser automation
- pytest and pytest-playwright as the test runner
- Page Object Model: page classes are in `pages/`, tests are in `tests/`

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run the tests
```bash
pytest                           # headless, Chromium
pytest --headed                  # watch the browser
pytest -k login                  # only login tests
pytest --browser firefox         # other browsers (install them first)
```
Screenshots of failing tests are saved to `test-results/`.

## Project structure
```
pages/            Page Object classes (locators and actions)
tests/            Test cases
conftest.py       Shared fixtures (logged_in)
pytest.ini        pytest settings
.github/workflows CI pipeline (GitHub Actions)
```

## Demo accounts
Password for all users: `secret_sauce`. Usernames: `standard_user`, `locked_out_user`, `problem_user`.

## Next steps
- Add checkout flow tests
- Add a cross-browser matrix in the CI workflow
- Add Allure reporting
