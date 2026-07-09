"""
Página do Menu Hamburger e navegação inicial.

IMPORTANTE: os locators abaixo (HAMBURGER e MENU_ITEM) são os MESMOS já validados
no projeto anterior (surf.robot), apenas convertidos de sintaxe Robot Framework
para Python/Appium. Não foram inventados — vieram do arquivo original que você
me enviou.
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

HAMBURGER = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')
MENU_ITEM_CLIQUE_SIMPLES = (
    AppiumBy.XPATH,
    '//*[@resource-id="com.qaxperience.yodapp:id/navView"]//*[@text="Clique em Botões"]'
)
MENU_ITEM_STAR_WARS = (
    AppiumBy.XPATH,
    '//*[@resource-id="com.qaxperience.yodapp:id/navView"]//*[@text="Star Wars"]'
)
MENU_ITEM_FORMULARIOS = (
    AppiumBy.XPATH,
    '//*[@resource-id="com.qaxperience.yodapp:id/navView"]//*[@text="Formulários"]'
)
MENU_ITEM_DIALOGS = (
    AppiumBy.XPATH,
    '//*[@resource-id="com.qaxperience.yodapp:id/navView"]//*[@text="Dialogs"]'
)
MENU_ITEM_CHECK_E_RADIO = (
    AppiumBy.XPATH,
    '//*[@resource-id="com.qaxperience.yodapp:id/navView"]//*[@text="Check e Radio"]'
)
START_TEXT = "QAX"


class MenuPage(BasePage):
    def get_started(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, f"//*[contains(@text, 'Yodapp')]"))
        )
        self.click_text(START_TEXT)

    def open_hamburger_menu(self):
        self.wait_and_click(HAMBURGER)

    def go_to_clique_simples_module(self):
        self.wait_and_click(MENU_ITEM_CLIQUE_SIMPLES)

    def go_to_star_wars_module(self):
        self.wait_and_click(MENU_ITEM_STAR_WARS)

    def go_to_formularios_module(self):
        self.wait_and_click(MENU_ITEM_FORMULARIOS)

    def go_to_dialogs_module(self):
        self.wait_and_click(MENU_ITEM_DIALOGS)

    def go_to_check_e_radio_module(self):
        self.wait_and_click(MENU_ITEM_CHECK_E_RADIO)
