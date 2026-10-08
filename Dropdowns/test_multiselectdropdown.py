import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_multi_select_dropdown(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")

    # Note: By using following three ways we can select the dropdown locator

    #page.locator("#multi-select").select_option(["Java","Python"])
    page.locator("#multi-select").select_option(label=["Java", "Python", "JavaScript", "C#"])  # By label
    #page.locator("#multi-select").select_option(value=["javascript","python"]) #By using value
    #page.locator("#multi-select").select_option(index=[1,3]) # By using Index
    dropdown_options=page.locator("#multi-select>option")
    items=[option.strip() for option in dropdown_options.all_text_contents()]
    print(items)
    page.wait_for_timeout(5000)