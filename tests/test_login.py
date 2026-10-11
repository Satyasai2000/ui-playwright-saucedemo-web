import re

import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"
INVENTORY_URL = re.compile(r".*/inventory\.html")


def test_valid_user_can_log_in(page):
    LoginPage(page).open().login("standard_user", PASSWORD)
    expect(page).to_have_url(INVENTORY_URL)
    expect(InventoryPage(page).title).to_have_text("Products")


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("unknown_user", PASSWORD, "Username and password do not match"),
        ("locked_out_user", PASSWORD, "this user has been locked out"),
        ("", PASSWORD, "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_login_shows_error(page, username, password, expected_error):
    LoginPage(page).open().login(username, password).expect_error(expected_error)
    expect(page).not_to_have_url(INVENTORY_URL)
