import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://wovonewqa.laborsolutions.tech/app/dashboard")
    page.wait_for_selector("text=Sign in to WOVO with your preferred method")
    page.get_by_role("link", name="WOVO ID WOVO ID").click()
    page.get_by_role("textbox", name="Username").fill("Kavya_Brand")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Wovo@123")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="My WOVO").click()
    page.get_by_role("button", name="Contacts").click()
    page.get_by_role("button", name="ADD NEW").click()
    page.get_by_role("textbox", name="ex: 123456").click()
    page.get_by_role("textbox", name="ex: 123456").fill("SAPBLR111")
    page.get_by_role("textbox", name="ex: John").click()
    page.get_by_role("textbox", name="ex: John").fill("sapblr111")
    page.locator("select").select_option("3106")
    page.get_by_role("button", name="SAVE").click()
    page.locator("span").filter(has_text="sapblr111").locator("div").first.click()
    page.locator("td > .hand > .info_round_checkbox").first.click()
    page.get_by_text("sapblr111", exact=True).click()
    page.get_by_role("textbox", name="ex: John").click()
    page.get_by_role("textbox", name="ex: John").fill("sapp19")
    page.get_by_role("textbox", name="ex: Doe").click()
    page.get_by_role("textbox", name="ex: Doe").fill("patil")
    page.get_by_role("button", name="SAVE").click()
    page.locator("span").filter(has_text="sapp19 patil").locator("div").first.click()
    
    page.get_by_role("button", name="KP").click()
    page.get_by_text("Logout").click()
    page.goto("https://ssoqa.laborsolutions.tech/realms/WOVO/protocol/openid-connect/auth?client_id=wovo-next&redirect_uri=https%3A%2F%2Fwovonewqa.laborsolutions.tech%2Fapp%2Fworker_contacts%2Flist&response_type=code&scope=openid&state=054c1b843f7f4cb8a8c5cbcfa0aced8b&code_challenge=8bG51Fsfctbo1wEVCQvmbxzIuVcqGRQRJy8CGsvXDf4&code_challenge_method=S256")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
