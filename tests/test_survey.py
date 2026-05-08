import re
from playwright.sync_api import Page, expect


def test_worker_contacts(page: Page):

    # ---------------- Login ----------------
    page.goto("https://wovonewqa.laborsolutions.tech/app/dashboard")
    page.get_by_text("Sign in to WOVO with your preferred method").wait_for()

    page.get_by_role("link", name="WOVO ID WOVO ID").click()
    page.get_by_role("textbox", name="Username").fill("Kavya_Brand")
    page.get_by_role("textbox", name="Password").fill("Wovo@123")
    page.get_by_role("button", name="Sign In").click()

    # ---------------- Create Survey ----------------
    page.get_by_role("button", name="Survey").click()
    page.get_by_role("button", name="Manage Surveys").click()
    page.get_by_role("button", name="ADD NEW").click()
    page.get_by_text("Create survey fresh").click()

    page.locator("#supported_languages_multiselect_chip_dropdown div") \
        .filter(has_text="Select...").nth(3).click()
    page.get_by_role("menuitem", name="-English").click()

    page.get_by_role("textbox", name="Survey Name ( 1-English ) *") \
        .fill("Playwright survey")

    page.locator("#reportingCategories_multiselect_chip_dropdown div") \
        .filter(has_text="Select...").nth(3).click()
    page.get_by_role("menuitem", name="187 - Communication").click()

    page.get_by_role("button", name="SAVE").click()
    page.get_by_role("button", name="eNPS").click()

    # ---------------- Add Question ----------------
    page.get_by_role("button", name="Question").click()

    page.get_by_role("button", name="Multiple Choice (Multi-Select)").click()
    page.get_by_role("option", name="Multiple Choice (Single-").click()

    question_box = page.locator("textarea").first
    expect(question_box).to_be_visible()
    question_box.fill("How are you?")

    option1 = page.locator("textarea[placeholder='Option 1']")
    option1.fill("Good")
    page.keyboard.press("Tab")

    option2 = page.locator("textarea[placeholder='Option 2']")
    option2.fill("Not good")
    page.keyboard.press("Tab")

    option3 = page.locator("textarea[placeholder='Option 3']")
    option3.fill("Great")

    # ---------------- Save Question ----------------
    save_btn = page.get_by_role("button", name="SAVE", exact=True)
    expect(save_btn).to_be_enabled()
    save_btn.click()

    page.locator("div").filter(has_text=re.compile(r"^Invite$")).click()
    page.locator("div").filter(
        has_text=re.compile(r"^Survey Period\*$")
    ).locator("div").nth(1).click()

    page.get_by_role("button", name="OK").click()

    # ---------------- Open Survey ----------------
    page.locator("#STATUS_DRAFT").select_option("1")

    page.get_by_text("Open this Survey").click()
    dialog = page.get_by_role("dialog")
    expect(dialog).to_be_visible()
    dialog.get_by_role("button", name="Open").click()

    # ---------------- Share Invite ----------------
    page.get_by_placeholder("Your text here...").fill("Kavya")
    page.locator("#SHARE_INVITES").click()

    # ---------------- Logout ----------------
    page.get_by_text("Survey Report").click()
    page.get_by_role("button", name="KP").click()
    page.get_by_text("Logout").click()
