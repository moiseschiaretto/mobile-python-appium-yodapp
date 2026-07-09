"""
Teste REAL do módulo Check e Radio > Checkbox.

Locators confirmados via Appium Inspector (tvTitle, checkboxButton
diferenciado por texto).
"""
from pages.menu_page import MenuPage
from pages.checkbox_page import CheckboxPage


def test_deve_marcar_e_desmarcar_um_checkbox(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_check_e_radio_module()

    checkbox = CheckboxPage(driver)
    checkbox.open_module()

    assert checkbox.is_loaded()

    checkbox.check("Python")
    assert checkbox.is_checked("Python") is True

    checkbox.uncheck("Python")
    assert checkbox.is_checked("Python") is False


def test_deve_marcar_multiplos_checkboxes_de_forma_independente(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_check_e_radio_module()

    checkbox = CheckboxPage(driver)
    checkbox.open_module()

    for opcao in ("Ruby", "Java", "Robot Framework"):
        checkbox.check(opcao)
        assert checkbox.is_checked(opcao) is True
