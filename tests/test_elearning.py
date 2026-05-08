import re
from playwright.sync_api import Page, expect

# ---------- Helper ----------
def do(page, action):
    action()
    page.wait_for_timeout(1000)  # 3 seconds after EVERY action


def test_worker_contacts(page: Page):

    do(page, lambda: page.goto("https://wovonewqa.laborsolutions.tech/app/dashboard"))
    page.wait_for_selector("text=Sign in to WOVO with your preferred method")

    do(page, lambda: page.get_by_role("link", name="WOVO ID WOVO ID").click())
    do(page, lambda: page.get_by_role("textbox", name="Username").fill("Kavya_Brand"))
    do(page, lambda: page.get_by_role("textbox", name="Password").fill("Wovo@123"))
    do(page, lambda: page.get_by_role("button", name="Sign In").click())

    do(page, lambda: page.get_by_role("button", name="E Learning").click())
    do(page, lambda: page.get_by_role("button", name="E Learning Reports").click())

    do(page, lambda: page.locator("button").nth(2).click())
    do(page, lambda: page.get_by_role("combobox").first.select_option("10"))

    do(page, lambda: page.get_by_role("button", name="18").click())
    do(page, lambda: page.get_by_role("button", name="24").click())
    do(page, lambda: page.get_by_role("button", name="OK").click())
    do(page, lambda: page.get_by_role("button", name="APPLY").click())

    do(page, lambda: page.get_by_text("Percentage").click())
    do(page, lambda: page.get_by_role("button", name="Download").click())

    # ---------- Download (DO NOT wrap inside do) ----------
    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.get_by_text("This page (XLSX)").click()
    download = download_info.value
    page1 = page1_info.value
    page1.close()
    page.wait_for_timeout(3000)

    do(page, lambda: page.get_by_role("button", name="Filters: Please select to").click())
    do(page, lambda: page.get_by_role("button", name="Open").nth(1).click())
    do(page, lambda: page.get_by_role("button", name="Deselect All").click())
    do(page, lambda: page.get_by_role("option", name="Worker").get_by_role("checkbox").check())

    do(page, lambda: page.locator("div").filter(
        has_text=re.compile(r"^Summary Table$")
    ).first.click())

    do(page, lambda: page.get_by_role("combobox", name="Department").click())
    do(page, lambda: page.get_by_text("All").nth(1).click())

    do(page, lambda: page.get_by_role("combobox", name="Locations").click())
    do(page, lambda: page.get_by_role("button", name="Deselect All").click())
    do(page, lambda: page.get_by_role("option", name="Airports").get_by_role("checkbox").check())
    do(page, lambda: page.get_by_text("CLEARAPPLY").click())
    
    do(page, lambda: page.get_by_role("combobox", name="Show").click())
    do(page, lambda: page.get_by_role("option", name="Enrolled").click())

    do(page, lambda: page.get_by_role("button", name="Open").nth(4).click())
    do(page, lambda: page.get_by_role("option", name="Gender").click())

    do(page, lambda: page.get_by_role("combobox", name="Lessons").click())
    do(page, lambda: page.get_by_role("option", name="了解申诉").click())
    do(page, lambda: page.get_by_role("checkbox").check())

    do(page, lambda: page.get_by_role("button", name="Deselect All").click())
    do(page, lambda: page.get_by_role("checkbox").check())
    do(page, lambda: page.get_by_role("button", name="APPLY").click())
    

    do(page, lambda: page.get_by_text("Percentage").click())
    do(page, lambda: page.get_by_role("button", name="Download").click())

    # ---------- Second Download ----------
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.get_by_text("This page (XLSX)").click()
    download1 = download1_info.value
    page2 = page2_info.value
    page2.close()
    page.wait_for_timeout(3000)

    do(page, lambda: page.get_by_role("button", name="KP").click())
    do(page, lambda: page.get_by_text("Logout").click())
