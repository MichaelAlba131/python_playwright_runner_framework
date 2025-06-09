from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_selector = 'input[name="email"]'
        self.password_selector = 'input[name="password"]'
        self.login_button_selector = '//button/div[text()="Entrar"]/ancestor::button'

    def open(self):
        self.page.goto("https://login.dafiti.com.br/")

    def get_username_input(self):
        return self.page.locator(self.username_selector)

    def get_password_input(self):
        return self.page.locator(self.password_selector)

    def get_login_button(self):
        return self.page.locator(self.login_button_selector)

    def get_title(self):
        return self.page.title()