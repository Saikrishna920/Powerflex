from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        # CSS selector targeting all the products links
        self.products_list_locator= "div#tbodyid div.card h4.card-title a"
        # Add to cart button (exact match using text)
        self.add_to_cart_button = page.locator(".btn.btn-success.btn-lg")
