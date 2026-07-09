"""
Página do módulo "Check e Radio" > "Botões de Radio".

Locators confirmados via Appium Inspector (imagens enviadas na conversa
"Automação mobile com Appium e Python"):
- Título da tela: com.qaxperience.yodapp:id/tvTitle (texto "Escolha sua
  linguagem preferida")
- Cada opção é um android.widget.RadioButton com resource-id COMPARTILHADO
  com.qaxperience.yodapp:id/radioButton entre todas as opções
  (Java, C#, Ruby, Python, Javascript, Elixir, Go Lang) -- diferenciadas
  pelo atributo text.

IMPORTANTE (bug conhecido e documentado do Appium/UiAutomator2, confirmado
em múltiplos issues oficiais do repositório appium/appium, ex: #6712 e
#3301): WebElement.is_selected() SEMPRE retorna False para
android.widget.CheckBox/RadioButton, independente do estado real marcado.
O atributo correto do UiAutomator2 pra esse caso é "checked", lido via
el.get_attribute("checked") (retorna a string "true"/"false"). Por isso os
métodos abaixo usam get_attribute("checked") em vez de is_selected().
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

TITLE = (AppiumBy.ID, "com.qaxperience.yodapp:id/tvTitle")


def _radio_locator(option_text):
    return (
        AppiumBy.XPATH,
        f'//android.widget.RadioButton[normalize-space(@text)="{option_text}"]',
    )


class RadioButtonPage(BasePage):
    def open_module(self):
        self.click_text("Botões de radio")

    def is_loaded(self):
        self.wait_visible(TITLE)
        return True

    def select_option(self, option_text):
        self.wait_and_click(_radio_locator(option_text))

    def is_selected(self, option_text):
        el = self.wait_visible(_radio_locator(option_text))
        return el.get_attribute("checked") == "true"
