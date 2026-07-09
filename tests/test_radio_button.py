"""
Teste REAL do módulo Check e Radio > Botões de Radio.

Locators confirmados via Appium Inspector (tvTitle, radioButton
diferenciado por texto).
"""
from pages.menu_page import MenuPage
from pages.radio_button_page import RadioButtonPage


def test_deve_selecionar_uma_opcao_de_radio(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_check_e_radio_module()

    radio = RadioButtonPage(driver)
    radio.open_module()

    assert radio.is_loaded()

    radio.select_option("Python")
    assert radio.is_selected("Python") is True


def test_deve_trocar_selecao_entre_opcoes(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_check_e_radio_module()

    radio = RadioButtonPage(driver)
    radio.open_module()

    radio.select_option("Java")
    assert radio.is_selected("Java") is True

    radio.select_option("Go Lang")
    assert radio.is_selected("Go Lang") is True
    assert radio.is_selected("Java") is False
