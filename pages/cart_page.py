class CartPage:
    def __init__(self, page):
        self.page = page
        self.item_names = page.locator(".cart_item .inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")
