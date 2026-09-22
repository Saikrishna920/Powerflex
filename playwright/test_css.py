from playwright.sync_api import Page, expect
import pytest
def test_css(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("T-shirts")
    page.get_by_role("button",name="Search").click()
    page.wait_for_timeout(5000)

    

