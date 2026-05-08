import re
from playwright.sync_api import Page, expect


def test_worker_contacts(page: Page):
   
    page.goto("https://wovonewqa.laborsolutions.tech/app/dashboard")
    page.wait_for_selector("text=Sign in to WOVO with your preferred method")
    
    page.get_by_role("link", name="WOVO ID WOVO ID").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Bhaskar-DA")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Wovo@123")
    page.get_by_role("button", name="Sign In").click()
    
    page.get_by_role("button", name="Connect").click()
    page.get_by_role("button", name="Case Management").click()
    page.get_by_role("textbox", name="Describe case here...").click()
    page.get_by_role("textbox", name="Describe case here...").fill("Hello Kavya")
   
    #page.get_by_text("Attach files").click()

# Upload file (THIS is the key fix)
    #page.set_input_files("input[type='file']", r"C:/Users/KavyashreePatil/Downloads/hello.xlsx")

    page.locator("div").filter(has_text=re.compile(r"^Gender$")).click()
    page.get_by_role("option", name="Male", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Birth Date$")).locator("path").click()
    page.locator("div").filter(has_text=re.compile(r"^Start Date$")).get_by_test_id("CalendarTodayOutlinedIcon").click()
    page.get_by_role("gridcell", name="29").click()
    page.get_by_role("button", name="SAVE").click()
    page.locator("div").filter(has_text=re.compile(r"^Birth Date$")).get_by_test_id("CalendarTodayOutlinedIcon").click()
    page.get_by_role("gridcell", name="8", exact=True).click()
    page.get_by_role("button", name="SAVE").click()
    page.locator("div").filter(has_text=re.compile(r"^Device Type$")).get_by_label("Open").click()
    page.get_by_role("option", name="Smartphone User", exact=True).click()
    page.get_by_role("combobox", name="Job Role").click()
    page.get_by_role("option", name="Worker").click()
    page.get_by_role("combobox", name="Department").click()
    page.get_by_role("option", name="afternoon").click()
    page.locator("div").filter(has_text=re.compile(r"^Locations$")).get_by_label("Open").click()
    page.get_by_role("option", name="Airports").get_by_role("checkbox").check()
    page.get_by_text("Case DetailSaveHello").click()
    page.get_by_role("combobox", name="Party in Charge Categories*").click()
    page.get_by_role("option", name="PIC1").click()
    page.get_by_role("combobox", name="Case Type").click()
    page.locator("div").filter(has_text=re.compile(r"^Party in Charge Categories\*$")).get_by_label("Open").click()
    page.get_by_role("option", name="HR").click()
    page.get_by_role("combobox", name="Case Type").click()
    page.get_by_role("option", name="WAGES AND INCENTIVES").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="BR").click()
    page.get_by_text("Logout").click()

    # ---------------------
   
