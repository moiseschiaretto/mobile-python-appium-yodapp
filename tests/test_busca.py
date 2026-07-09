"""
Teste REAL do módulo Star Wars > Busca.

Navegação e carregamento da tela confirmados via Appium Inspector.
O passo de digitação (buscar) usa um locator inferido por classe, não
confirmado no Inspector -- ver docstring de pages/busca_page.py. Se este
teste falhar no passo de digitação, é o ponto a revalidar primeiro.
"""
from pages.menu_page import MenuPage
from pages.busca_page import BuscaPage


def test_deve_pesquisar_personagem_star_wars(driver):
    menu = MenuPage(driver)
    menu.get_started()
    menu.open_hamburger_menu()
    menu.go_to_star_wars_module()

    busca = BuscaPage(driver)
    busca.open_module()

    assert busca.is_loaded()
    busca.buscar("Chewbacca")
    assert busca.is_result_visible("Chewbacca")
