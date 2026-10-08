import pytest
from playwright.sync_api import Page,expect

def test_checkbox(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #1. select specific check box(Sunday)
    sunday=page.get_by_label("Sunday")
    sunday.check()
    expect(sunday).to_be_checked()
    page.wait_for_timeout(5000)

    #2. count number of checkboxes:



