"""
Testes do módulo "Clique em Botões".

test_deve_realizar_um_clique_simples -- porta direta do cenário já validado
no projeto anterior (surf.robot).

test_deve_realizar_um_clique_longo -- corrigido: "Clique em Botões" tem dois
cards separados ("Clique simples" e "Clique longo"), cada um levando a uma
tela diferente. O teste precisa navegar pelo card "Clique longo"
(open_module_longo), não pelo card "Clique simples" -- esse era o motivo
real do NoSuchElementError reportado (o botão long_click não existe na tela
de Clique Simples).
"""
from pages.menu_page import MenuPage
from pages.simple_click_page import SimpleClickPage


def test_deve_realizar_um_clique_simples(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_clique_simples_module()

    click_page = SimpleClickPage(driver)
    click_page.open_module()
    click_page.click_button()


def test_deve_realizar_um_clique_longo(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_clique_simples_module()

    click_page = SimpleClickPage(driver)
    click_page.open_module_longo()
    click_page.long_click_button()
