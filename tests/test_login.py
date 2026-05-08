import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://ssoqa.laborsolutions.tech/realms/WOVO/protocol/openid-connect/auth?client_id=wovo-next&redirect_uri=https%3A%2F%2Fwovonewqa.laborsolutions.tech%2Fapp%2Fdashboard&response_type=code&scope=openid&state=3f63724f48a44d9c812e3540c03d8d3b&code_challenge=Ol2agXen1Dc-bN5R8sHXz1ZSDQn0mo5UbCTBSUvtAuY&code_challenge_method=S256")
    page.get_by_role("link", name="WOVO ID WOVO ID").click()
    page.get_by_role("textbox", name="Username").fill("Kavya_Brand")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Wovo@123")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="KP").click()
    page.get_by_text("Logout").click()
    expect(page.get_by_role("link", name="WOVO ID WOVO ID")).to_be_visible()
    expect(page.locator("#social-python")).to_contain_text("WOVO ID")
    expect(page.locator("#social-python")).to_match_aria_snapshot("- text: WOVO ID")
