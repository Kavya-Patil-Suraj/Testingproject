import re
from playwright.sync_api import Page, sync_playwright, expect
from pages.Wovo_loginpage import loginpage
from pages.Wovo_homepage import homepage_Wovo

def test_example(page: Page) -> None:
    page.goto("https://wovonewqa.laborsolutions.tech/app/dashboard")

loginpage = loginpage(Page)
homepage_Wovo = homepage_Wovo(Page)

loginpage.enter_username("Kavya_Brand")
loginpage.enter_password("Wovo@123")
loginpage.click_signin()

homepage_Wovo.select_client_dropdown
homepage_Wovo.select_client
homepage_Wovo.client_input
homepage_Wovo.client_option.click()

