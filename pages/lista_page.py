"""
Página do módulo Star Wars > Lista.

Locators confirmados via Appium Inspector (screenshots enviados):
- Toolbar com botão voltar (ivBack) e título "Lista" (toolbarTitle)
- RecyclerView de personagens: resource-id "rvList"
- Botão flutuante de adicionar: resource-id "fab"

Os nomes dos personagens (ex.: "Mandaloriano", "Darth Vader") são visíveis na
tela mas o Inspector não expandiu o resource-id da TextView interna do item
(a árvore parou em container/drag_handle/indicator/image_view). Por isso a
seleção de item usa busca por texto (mesmo padrão já usado em menu_page.py
para os itens do menu principal), não por resource-id.
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

TOOLBAR_TITLE = (AppiumBy.ID, "com.qaxperience.yodapp:id/toolbarTitle")
BACK_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/ivBack")
RV_LIST = (AppiumBy.ID, "com.qaxperience.yodapp:id/rvList")
FAB_ADD = (AppiumBy.ID, "com.qaxperience.yodapp:id/fab")


class ListaPage(BasePage):
    def open_module(self):
        # Clica no item "Lista" do submenu Star Wars (tvItemTitle)
        self.click_text("Lista")

    def is_loaded(self):
        self.wait_visible(TOOLBAR_TITLE)
        self.wait_visible(RV_LIST)
        return True

    def select_item(self, nome_personagem):
        """Clica no personagem pelo texto visível (ex.: 'Mandaloriano')."""
        self.click_text(nome_personagem)

    def is_item_visible(self, nome_personagem):
        try:
            self.find_by_text(nome_personagem)
            return True
        except Exception:
            return False

    def open_add_dialog(self):
        self.wait_and_click(FAB_ADD)

    def go_back(self):
        self.wait_and_click(BACK_BUTTON)
