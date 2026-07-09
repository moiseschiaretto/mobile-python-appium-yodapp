"""
Página do módulo "Login".

Locators confirmados via Appium Inspector (chat "Configuração do projeto
mobile com Appium e Python"):
- Email: com.qaxperience.yodapp:id/etEmail
- Senha: com.qaxperience.yodapp:id/etPassword
- Botão Entrar: com.qaxperience.yodapp:id/btnSubmit
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

EMAIL_FIELD = (AppiumBy.ID, "com.qaxperience.yodapp:id/etEmail")
PASSWORD_FIELD = (AppiumBy.ID, "com.qaxperience.yodapp:id/etPassword")
SUBMIT_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/btnSubmit")


class LoginPage(BasePage):
    def open_module(self):
        self.click_text("Login")

    def login(self, email, senha):
        self.wait_visible(EMAIL_FIELD).send_keys(email)
        self.wait_visible(PASSWORD_FIELD).send_keys(senha)
        self.wait_and_click(SUBMIT_BUTTON)

    def is_loaded(self):
        self.wait_visible(EMAIL_FIELD)
        self.wait_visible(PASSWORD_FIELD)
        return True
