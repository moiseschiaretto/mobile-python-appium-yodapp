"""
Teste REAL do módulo Formulários > Cadastro.

Locators confirmados via Appium Inspector (etUsername, etEmail, etPassword,
spinnerJob, btnSubmit).
"""
from pages.menu_page import MenuPage
from pages.cadastro_page import CadastroPage


def test_deve_exibir_tela_de_cadastro(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_formularios_module()

    cadastro = CadastroPage(driver)
    cadastro.open_module()

    assert cadastro.is_loaded()


def test_deve_preencher_e_submeter_cadastro(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_formularios_module()

    cadastro = CadastroPage(driver)
    cadastro.open_module()
    cadastro.preencher_formulario({
        "nome": "Moises QA",
        "email": "moises.qa@qaxperience.com",
        "senha": "senha123",
    })
    cadastro.submeter()
