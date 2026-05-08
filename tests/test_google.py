import re
from playwright.sync_api import expect
def test_google_title(page):
    page.wait_for_timeout(5000)
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
    except:
        print("No popup to accept")
    page.get_by_role("combobox", name="search").fill("Playwright python")
    
    page.keyboard.press("Enter")
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))