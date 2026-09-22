from playwright.sync_api import Playwright,sync_playwright,Page
import datetime

def test_screenshort_demo(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Partial Page screenshot (visible on the page)
    #page.screenshot(path=f"screenshorts/homepage.png_{timestamp}.png")

    # Full Page screenshort
    #page.screenshot(path=f"screenshorts/homepage.png_{timestamp}.png",full_page=True)

    #Element/Specific section of the page screenshort
    #logo=page.locator(".header-logo").screenshot(path=f"screenshorts/logo.png_{timestamp}.png")
 

