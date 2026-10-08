import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_browser_stack(page: Page):
    page.goto("https://bstackdemo.com/")
    order=page.locator("//div[@class='sort']//select").select_option(value="lowestprice")
    items=page.locator(".shelf-container>div")
    elements=[i.strip() for i in items.all_text_contents()]
    print(elements)


    page.wait_for_timeout(5000)
