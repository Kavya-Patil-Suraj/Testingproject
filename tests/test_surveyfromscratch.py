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
    
    page.get_by_role("button", name="Survey").click()
    page.get_by_role("button", name="Manage Surveys").click()
    page.get_by_role("button", name="Filter").click()
    page.get_by_role("textbox", name="Survey").click()
    page.get_by_role("textbox", name="Survey").fill("cross tab")
    page.get_by_role("button", name="APPLY").click()
    page.get_by_role("row", name="Brand Survey from scratch:").locator("svg").click()
    page.wait_for_timeout(3000)
    page.get_by_text("View Report").click()
    page.wait_for_timeout(3000)
    page.locator("#app-site iframe").content_frame.get_by_role("button", name="Charts").click()
    page.wait_for_timeout(3000)
    page.locator("#app-site iframe").content_frame.get_by_role("menuitem", name="Table").click()
    page.wait_for_timeout(3000)
    page.locator("#app-site iframe").content_frame.get_by_role("button", name="Charts").click()
    page.wait_for_timeout(3000)
    page.locator("#app-site iframe").content_frame.get_by_role("menuitem", name="Table").click()
    page.wait_for_timeout(3000)
 
    
    page.locator("#app-site iframe").content_frame.get_by_role("option", name="Gender (WOVO)").click()
    page.wait_for_timeout(1000)
    page.locator("#app-site iframe").content_frame.get_by_role("combobox", name="Group by Gender (WOVO)").click()
    page.locator("#app-site iframe").content_frame.get_by_role("option", name="Age Group (WOVO)").click()
    page.locator("#app-site iframe").content_frame.get_by_role("combobox", name="Group by Age Group (WOVO)").click()
    page.locator("#app-site iframe").content_frame.get_by_role("option", name="New Single select").click()
    page.locator("#app-site iframe").content_frame.get_by_role("combobox", name="View data by Questions").click()
    page.locator("#app-site iframe").content_frame.get_by_role("option", name="Categories").click()
    page.locator("#app-site iframe").content_frame.get_by_role("combobox", name="Group by New Single select").click()
    page.locator("#app-site iframe").content_frame.get_by_role("option", name="Gender (WOVO)").click()
    page.locator("#app-site iframe").content_frame.get_by_role("button", name="Download").click()
    with page.expect_download() as download_info:
        page.locator("#app-site iframe").content_frame.get_by_role("menuitem", name="This page (XLS)").click()
    download = download_info.value
    page.locator("#app-site iframe").content_frame.get_by_role("button", name="Download").click()
    with page.expect_download() as download1_info:
        page.locator("#app-site iframe").content_frame.get_by_text("Raw Data (XLSX)").click()
    download1 = download1_info.value
    page.get_by_role("button", name="ADD NEW").click()
    page.get_by_text("Create survey fresh").click()
    page.locator("#supported_languages_multiselect_chip_dropdown div").filter(has_text="Select...").nth(3).click()
    page.get_by_role("menuitem", name="-English").click()
    page.get_by_role("textbox", name="Survey Name ( 1-English ) *").click()
    page.get_by_role("textbox", name="Survey Name ( 1-English ) *").fill("Playwright survey")
    page.locator("#reportingCategories_multiselect_chip_dropdown div").filter(has_text="Select...").nth(3).click()
    page.get_by_role("menuitem", name="187 - Communication").click()
    page.get_by_role("button", name="SAVE").click()
    page.get_by_role("button", name="eNPS").click()
    page.wait_for_timeout(3000)
    # Open Question builder
    page.get_by_role("button", name="Question").click()
    page.wait_for_timeout(3000)

# Select question type
    page.get_by_role("button", name="Multiple Choice (Multi-Select)").click()
    page.wait_for_timeout(3000)
    page.get_by_role("option", name="Multiple Choice (Single-").click()

# Wait for editor to fully settle after dropdown close
    page.wait_for_timeout(3000)

# ---------- Question text ----------
    question_box = page.locator("textarea").nth(0)
    expect(question_box).to_be_visible(timeout=15000)
    question_box.click()
    question_box.type("How are you?", delay=50)

# ---------- Option 1 ----------
    option1 = page.locator("textarea[placeholder='Option 1']")
    expect(option1).to_be_visible(timeout=15000)
    option1.click()
    option1.type("Good", delay=50)

# Trigger React to create Option 2
    page.keyboard.press("Tab")

# ---------- Option 2 ----------
    option2 = page.locator("textarea[placeholder='Option 2']")
    expect(option2).to_be_visible(timeout=15000)
    option2.click()
    option2.type("Not good", delay=50)

# Trigger React to create Option 3
    page.keyboard.press("Tab")

# ---------- Option 3 ----------
    option3 = page.locator("textarea[placeholder='Option 3']")
    expect(option3).to_be_visible(timeout=15000)
    option3.click()
    option3.type("Great", delay=50)

    page.keyboard.press("Tab")

    # ---------- Save Question ----------
    save_btn = page.get_by_role("button", name="SAVE", exact=True)

    expect(save_btn).to_be_enabled()
    save_btn.click()
    page.locator("div").filter(has_text=re.compile(r"^Invite$")).click()
    page.locator("div").filter(has_text=re.compile(r"^Survey Period\*$")).locator("div").nth(1).click()
    
    page.get_by_role("button", name="OK").click()

    page.locator("#STATUS_DRAFT").select_option("1")

# Confirm opening survey
    page.get_by_text("Open this Survey").click()
    dialog = page.get_by_role("dialog")
    dialog.get_by_role("button", name="Open").click()
    page.get_by_placeholder("Your text here...").click()
    page.get_by_placeholder("Your text here...").fill("Kavya")
    page.locator("#SHARE_INVITES").click()
    page.get_by_role("heading").locator("div").nth(1).click()
    page.get_by_text("Survey Report").click()
    
    page.get_by_role("button", name="KP").click()
    page.get_by_text("Logout").click()