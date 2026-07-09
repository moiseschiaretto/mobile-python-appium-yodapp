"""
Página do módulo Star Wars > Busca.

Locators confirmados via Appium Inspector (screenshots enviados):
- Toolbar com botão voltar (ivBack) e título "Busca" (toolbarTitle)
- Container do campo de busca: resource-id "frmSearch" (ViewGroup)
- RecyclerView de resultados: resource-id "rvList" (mesmo id da tela Lista)

ATENÇÃO - NÃO CONFIRMADO: o Inspector não expandiu o elemento interno
editável dentro de "frmSearch" (provável androidx SearchView / EditText
nativo). O locator SEARCH_INPUT abaixo foi inferido por classe Android
padrão, não por resource-id capturado. Validar no emulador antes de usar
em CI -- se falhar, reabrir o Appium Inspector, clicar no campo "Busque
aqui" e capturar o resource-id real do elemento focado.
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

TOOLBAR_TITLE = (AppiumBy.ID, "com.qaxperience.yodapp:id/toolbarTitle")
BACK_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/ivBack")
SEARCH_CONTAINER = (AppiumBy.ID, "com.qaxperience.yodapp:id/frmSearch")
RV_LIST = (AppiumBy.ID, "com.qaxperience.yodapp:id/rvList")
# Inferido, não confirmado no Inspector - ver docstring acima.
SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")


class BuscaPage(BasePage):
    def open_module(self):
        # Clica no item "Busca" do submenu Star Wars (tvItemTitle)
        self.click_text("Busca")

    def is_loaded(self):
        self.wait_visible(TOOLBAR_TITLE)
        self.wait_visible(SEARCH_CONTAINER)
        return True

    def buscar(self, termo):
        """Digita o termo no campo de busca.

        Locator do campo (SEARCH_INPUT) ainda não confirmado via Inspector
        -- ver docstring do módulo. Validar antes de confiar no CI.
        """
        campo = self.wait_visible(SEARCH_INPUT)
        campo.send_keys(termo)

    def is_result_visible(self, nome_personagem):
        try:
            self.find_by_text(nome_personagem)
            return True
        except Exception:
            return False

    def go_back(self):
        self.wait_and_click(BACK_BUTTON)
