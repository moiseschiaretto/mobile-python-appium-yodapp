"""
Teste REAL do módulo Star Wars > Lista.

Locators confirmados via Appium Inspector (menu, submenu Star Wars, tela
Lista com rvList/fab/toolbarTitle). Nomes de personagem são localizados
por texto visível, já que o Inspector não expôs resource-id próprio para
essas TextViews (ver docstring de pages/lista_page.py).
"""
from pages.menu_page import MenuPage
from pages.lista_page import ListaPage


def test_deve_exibir_lista_de_personagens_star_wars(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_star_wars_module()

    lista = ListaPage(driver)
    lista.open_module()

    assert lista.is_loaded()
    assert lista.is_item_visible("Mandaloriano")
    assert lista.is_item_visible("Darth Vader")
    assert lista.is_item_visible("Chewbacca")


def test_deve_selecionar_um_personagem_na_lista(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_star_wars_module()

    lista = ListaPage(driver)
    lista.open_module()
    lista.is_loaded()

    lista.select_item("Princesa Leia")
