"""
Página do módulo "Check e Radio" > "Checkbox".

Locators confirmados via Appium Inspector (imagens enviadas na conversa
"Automação mobile com Appium e Python"):
- Título da tela: com.qaxperience.yodapp:id/tvTitle (texto "Marque as
  techs que usam Appium")
- Cada opção é um android.widget.CheckBox com resource-id COMPARTILHADO
  com.qaxperience.yodapp:id/checkboxButton entre todas as opções
  (Ruby, Python, Java, Javascript, Cobol, C#, Robot Framework) --
  a única forma de diferenciar uma da outra é pelo atributo text.

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


def _checkbox_locator(option_text):
    return (
        AppiumBy.XPATH,
        f'//android.widget.CheckBox[normalize-space(@text)="{option_text}"]',
    )


class CheckboxPage(BasePage):
    def open_module(self):
        self.click_text("Checkbox")

    def is_loaded(self):
        self.wait_visible(TITLE)
        return True

    def check(self, option_text):
        el = self.wait_visible(_checkbox_locator(option_text))
        if el.get_attribute("checked") != "true":
            el.click()

    def uncheck(self, option_text):
        el = self.wait_visible(_checkbox_locator(option_text))
        if el.get_attribute("checked") == "true":
            el.click()

    def is_checked(self, option_text):
        el = self.wait_visible(_checkbox_locator(option_text))
        return el.get_attribute("checked") == "true"
