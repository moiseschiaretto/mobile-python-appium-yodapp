"""
Classe base do Page Object Model.
Métodos comuns reutilizados por todas as páginas.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_click(self, locator):
        el = self.wait_visible(locator)
        el.click()
        return el

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_by_text(self, text):
        return self.driver.find_element(
            AppiumBy.XPATH, f"//*[@text='{text}']"
        )

    def click_text(self, text):
        self.find_by_text(text).click()

    def long_press(self, locator, duration_ms=1000):
        """Pressão longa via mobile gesture nativo do UiAutomator2.
        TouchAction foi removido no Appium-Python-Client 5.x, então usamos
        o comando 'mobile: longClickGesture' (padrão atual recomendado)."""
        el = self.wait_visible(locator)
        self.driver.execute_script(
            "mobile: longClickGesture",
            {"elementId": el.id, "duration": duration_ms}
        )
