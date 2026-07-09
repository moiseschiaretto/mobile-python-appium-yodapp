"""
Página do módulo "Cadastro".

Locators confirmados via Appium Inspector (chat "Configuração do projeto
mobile com Appium e Python"):
- Nome: com.qaxperience.yodapp:id/etUsername
- Email: com.qaxperience.yodapp:id/etEmail
- Senha: com.qaxperience.yodapp:id/etPassword
- Dropdown Nível: com.qaxperience.yodapp:id/spinnerJob
- Botão Cadastrar: com.qaxperience.yodapp:id/btnSubmit
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

NOME_FIELD = (AppiumBy.ID, "com.qaxperience.yodapp:id/etUsername")
EMAIL_FIELD = (AppiumBy.ID, "com.qaxperience.yodapp:id/etEmail")
SENHA_FIELD = (AppiumBy.ID, "com.qaxperience.yodapp:id/etPassword")
NIVEL_DROPDOWN = (AppiumBy.ID, "com.qaxperience.yodapp:id/spinnerJob")
SUBMIT_BUTTON = (AppiumBy.ID, "com.qaxperience.yodapp:id/btnSubmit")


class CadastroPage(BasePage):
    def open_module(self):
        self.click_text("Cadastro")

    def preencher_formulario(self, dados: dict):
        """dados esperado: {'nome': str, 'email': str, 'senha': str}"""
        self.wait_visible(NOME_FIELD).send_keys(dados["nome"])
        self.wait_visible(EMAIL_FIELD).send_keys(dados["email"])
        self.wait_visible(SENHA_FIELD).send_keys(dados["senha"])

    def selecionar_nivel(self, nivel_texto):
        self.wait_and_click(NIVEL_DROPDOWN)
        self.click_text(nivel_texto)

    def submeter(self):
        self.wait_and_click(SUBMIT_BUTTON)

    def is_loaded(self):
        self.wait_visible(NOME_FIELD)
        return True
