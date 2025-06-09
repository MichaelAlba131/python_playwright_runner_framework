from pages.login_page import LoginPage
from interactions.LoginInteractions import LoginInteractions

def test_successful_login(page):
    login_page = LoginPage(page)
    login_interactions = LoginInteractions(login_page)
    print("Iniciando teste de login")
    login_page.open()
    login_interactions.login("teste@teste.com", "senha_invalida")
    login_interactions.valido_a_mensagem_na_tela("Dados incorretos")