"""
Página do módulo "Dialogs" (chamado "Diálogo" internamente no projeto).

Locators confirmados via Appium Inspector (chat "Configuração do projeto
mobile com Appium e Python"):
- Título do popup: com.qaxperience.yodapp:id/dialogInfoTitle
- Subtítulo: com.qaxperience.yodapp:id/dialogInfoSubtitle
- Texto: com.qaxperience.yodapp:id/dialogInfoText
- Botão OK: com.qaxperience.yodapp:id/dialogInfoOk

Nota: o item que abre o diálogo é o card de lista com texto "Info"
(resource-id tvItemTitle, texto "Info"), por isso a abertura usa
click_text("Info") em vez de um id fixo do card.
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

DIALOG_TITLE = (AppiumBy.ID, "com.qaxperience.yodapp:id/dialogInfoTitle")
DIALOG_SUBTITLE = (AppiumBy.ID, "com.qaxperience.yodapp:id/dialogInfoSubtitle")
DIALOG_TEXT = (AppiumBy.ID, "com.qaxperience.yodapp:id/dialogInfoText")
DIALOG_OK_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/dialogInfoOk")


class DialogoPage(BasePage):
    def open_module(self):
        self.click_text("Dialogs")

    def abrir_dialogo(self):
        self.click_text("Info")
        self.wait_visible(DIALOG_TITLE)

    def get_titulo(self):
        return self.find(DIALOG_TITLE).text

    def confirmar(self):
        self.wait_and_click(DIALOG_OK_BUTTON)
