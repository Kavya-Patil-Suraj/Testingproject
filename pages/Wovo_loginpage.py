from playwright.sync_api import Page, sync_playwright

class loginpage:
    
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.signin_button = page.get_by_role("button", name="Sign In")
        
        def enter_username(self, username:str):
            self.username_input.fill(username)
            
        def enter_password(self, password:str):
            self.password_input.fill(password)
            
        def click_signin(self):
            self.signin_button.click()