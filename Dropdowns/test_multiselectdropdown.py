import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_multiselectdropdown(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")

    #select multiple options from the dropdown:
    #page.locator("#multi-select").select_option(["Java","Python"])
    #page.locator("#multi-select").select_option(label=["Java", "Python", "JavaScript", "C#"])  # By label
    #page.locator("#multi-select").select_option(value=["javascript","python"]) #By using value
    page.locator("#multi-select").select_option(index=[1,3]) # By using Index
    page.wait_for_timeout(5000)