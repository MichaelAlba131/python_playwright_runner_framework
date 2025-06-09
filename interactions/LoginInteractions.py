import time
from pages.login_page import LoginPage
from utils.Utils import Utils

class LoginInteractions:
    def __init__(self, login_page: LoginPage):
        self.login_page = login_page

    def login(self, username, password):
        Utils.wait_for_element(lambda: self.login_page.get_username_input()).fill(username)
        print("Preenche usuario:" + username)
        Utils.wait_for_element(lambda: self.login_page.get_password_input()).fill(password)
        print("Preenche senha:" + password)
        Utils.wait_for_element(lambda: self.login_page.get_login_button()).click()
        print("Clica em Entrar")
    def valido_a_mensagem_na_tela(self, mensagem):
        return Utils.wait_for_text(self.login_page.page, mensagem, 10)