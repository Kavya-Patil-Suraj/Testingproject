from playwright.sync_api import sync_playwright

def test_wovo_title():
    with sync_playwright() as p:
        # Launch browser in headful mode
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the WOVO site
        page.goto("https://wovonew.laborsolutions.tech/")

        # Get the page title
        title = page.title()
        print(f"Page title: {title}")

        # Assert the title (update expected title if needed)
        expected_title_keyword = "Wovo"  # Replace this with the actual expected keyword
        assert expected_title_keyword in title, f"Expected '{expected_title_keyword}' in title, but got '{title}'"

        # Close browser
        browser.close()
