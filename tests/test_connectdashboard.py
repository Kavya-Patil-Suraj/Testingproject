import re
from playwright.sync_api import Page, expect


def test_worker_contacts(page: Page):
   
    page.goto("https://wovonewqa.laborsolutions.tech/app/dashboard")
    page.wait_for_selector("text=Sign in to WOVO with your preferred method")
    
    page.get_by_role("link", name="WOVO ID WOVO ID").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Kavya_Brand")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Wovo@123")
    page.get_by_role("button", name="Sign In").click()
    
    page.get_by_role("button", name="Dashboard").click()
    page.get_by_role("button", name="Connect").click()
    page.get_by_role("button", name="Connect Reports").click()
    page.get_by_role("button", name="Filters").click()
    page.get_by_role("combobox").nth(1).select_option("ask")
    page.get_by_role("combobox").nth(2).select_option("app")
    page.get_by_role("button", name="APPLY").click()
    page.wait_for_timeout(5000)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.get_by_role("button", name="Incoming").click()
    page.get_by_text("Outgoing", exact=True).click()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.get_by_role("button", name="Download").click()
    with page.expect_download() as download_info:
        page.get_by_text("This page (PDF)").click()
    download = download_info.value
    page.get_by_role("button", name="Download").click()
    with page.expect_download() as download1_info:
        with page.expect_popup() as page1_info:
            page.get_by_text("Raw Data (XLSX)").click()
        page1 = page1_info.value
    download1 = download1_info.value
    page1.close()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Outgoing").click()
    page.wait_for_timeout(5000)
    page.get_by_text("Summary Table").click()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.get_by_label("Group by").select_option("gender")
    page.get_by_role("button", name="Download").click()
    with page.expect_download() as download2_info:
        with page.expect_popup() as page2_info:
            page.get_by_text("Raw Data (XLSX)").click()
        page2 = page2_info.value
    download2 = download2_info.value
    page2.close()
    page.get_by_role("button", name="KP").click()
    page.get_by_text("Logout").click()
