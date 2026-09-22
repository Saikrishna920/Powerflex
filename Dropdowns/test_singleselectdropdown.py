import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_singleselectdropdown(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")
    #Note: By using following three ways we can able to select the dropdown locator

    #page.locator("#standard-select").select_option(value="green")
    #page.locator("#standard-select").select_option(label="Green")
    page.locator("#standard-select").select_option(index=2) #Here, index starts from 0. we can select based on corresponding index.

    #check number of options in dropdown
    dropdown_options=page.locator("#standard-select")
    names=[i.strip() for i in dropdown_options.all_text_contents()]
    print(names)
    page.wait_for_timeout(5000)