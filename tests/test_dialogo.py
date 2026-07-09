"""
Teste REAL do módulo Dialogs.

Locators confirmados via Appium Inspector (dialogInfoTitle, dialogInfoOk).
"""
from pages.menu_page import MenuPage
from pages.dialogo_page import DialogoPage


def test_deve_abrir_e_confirmar_dialogo_info(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_dialogs_module()

    dialogo = DialogoPage(driver)
    dialogo.abrir_dialogo()

    assert dialogo.get_titulo() != ""
    dialogo.confirmar()
