"""
Página do módulo "Clique em Botões".

IMPORTANTE (corrigido com base nos prints reais do Appium Inspector):
"Clique em Botões" abre uma tela com DOIS CARDS -- "Clique simples" e
"Clique longo" -- cada um levando a uma TELA SEPARADA, cada uma com seu
próprio botão. Não é a mesma tela com dois botões. Por isso existem dois
métodos de navegação distintos: open_module_simples() e open_module_longo().

Locators confirmados via Appium Inspector:
- Card "Clique simples" / "Clique longo": tvItemTitle, diferenciado por texto
- Botão na tela "Clique Simples": com.qaxperience.yodapp:id/short_click
- Botão na tela "Botão clique longo": com.qaxperience.yodapp:id/long_click
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

BOTAO_CLIQUE_SIMPLES_TEXT = "CLIQUE SIMPLES"
SHORT_CLICK_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/short_click")
LONG_CLICK_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/long_click")


class SimpleClickPage(BasePage):
    def open_module(self):
        self.click_text("Clique simples")

    def open_module_longo(self):
        self.click_text("Clique longo")

    def click_button(self):
        self.click_text(BOTAO_CLIQUE_SIMPLES_TEXT)

    def long_click_button(self):
        self.long_press(LONG_CLICK_BUTTON)
