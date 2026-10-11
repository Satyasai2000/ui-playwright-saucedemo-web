class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator(".product_sort_container")

    def add_to_cart(self, product_slug: str):
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()
        return self

    def remove_from_cart(self, product_slug: str):
        self.page.locator(f"[data-test='remove-{product_slug}']").click()
        return self

    def open_cart(self):
        self.cart_link.click()

    def sort_by(self, option: str):
        """option: 'az', 'za', 'lohi' (price low to high), or 'hilo'."""
        self.sort_dropdown.select_option(option)
        return self

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.item_prices.all_inner_texts()]
