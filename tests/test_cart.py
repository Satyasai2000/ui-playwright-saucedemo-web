from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


def test_adding_one_item_sets_badge_to_1(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK)
    expect(inventory.cart_badge).to_have_text("1")


def test_adding_two_items_sets_badge_to_2(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK).add_to_cart(BIKE_LIGHT)
    expect(inventory.cart_badge).to_have_text("2")


def test_removing_item_clears_badge(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK).remove_from_cart(BACKPACK)
    expect(inventory.cart_badge).to_have_count(0)


def test_cart_shows_added_item(logged_in):
    inventory = InventoryPage(logged_in)
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()
    expect(CartPage(logged_in).item_names).to_have_text(["Sauce Labs Backpack"])


def test_sort_by_price_low_to_high(logged_in):
    inventory = InventoryPage(logged_in).sort_by("lohi")
    prices = inventory.prices()
    assert prices == sorted(prices)


def test_sort_by_name_z_to_a(logged_in):
    inventory = InventoryPage(logged_in).sort_by("za")
    names = inventory.names()
    assert names == sorted(names, reverse=True)
