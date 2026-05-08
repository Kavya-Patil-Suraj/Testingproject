
from playwright.sync_api import Page, sync_playwright, expect
class homepage_Wovo:
    def __init__(self, page):
        self.page = page
        self.select_client_dropdown = page.get_by_role("combobox", name="Select Client").click()
        self.close_button = page.get_by_role("button", name="Close").click()
        self.client_input = page.get_by_role("combobox", name="Select Client").fill 
        self.client_option = page.get_by_role("option", name="Wovo Demo-Child2").click()
        
    def is_loaded(self):
         return self.page.wait_for_selector("text=Sign in to WOVO with your preferred method")   
     
    def select_client(self, client_name:str):
        self.client_input(client_name)
        self.client_option.click()
        
   