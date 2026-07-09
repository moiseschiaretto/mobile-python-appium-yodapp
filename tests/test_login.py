"""
Teste REAL do módulo Formulários > Login.

Locators confirmados via Appium Inspector (etEmail, etPassword, btnSubmit).
"""
from pages.menu_page import MenuPage
from pages.login_page import LoginPage


def test_deve_exibir_tela_de_login(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_formularios_module()

    login = LoginPage(driver)
    login.open_module()

    assert login.is_loaded()


def test_deve_preencher_login(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_formularios_module()

    login = LoginPage(driver)
    login.open_module()
    login.login("teste@qaxperience.com", "senha123")
