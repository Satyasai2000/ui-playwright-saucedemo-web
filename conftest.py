import re

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


@pytest.fixture
def logged_in(page):
    """Open the site and log in as a standard user."""
    LoginPage(page).open().login("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    return page
