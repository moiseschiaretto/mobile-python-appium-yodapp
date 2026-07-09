"""
Configuração central do pytest + Appium.

As capabilities abaixo replicam exatamente o que já estava validado no projeto
anterior (surf.robot): mesmo app, mesmo emulador, mesma automationName.

O driver é criado por teste (scope="function"): o app abre no início de cada
teste e fecha no final. Uma tentativa anterior de reaproveitar uma única
sessão (scope="session" + terminate_app/activate_app) foi revertida porque
o app, ao ser reaberto dessa forma, não exibe a splash inicial de novo
("Yodapp" / botão "QAX"), quebrando o get_started() em todos os testes
exceto o primeiro. Esta é a configuração validada e funcional.
"""
import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

APP_PATH = os.path.join(os.path.dirname(__file__), "app", "yodapp-beta.apk")


def pytest_html_report_title(report):
    report.title = "Yodapp Mobile — Relatório de Execução (Python + Appium)"


def pytest_html_results_table_header(cells):
    del cells[-1]  # remove coluna "Links" (não usada — nenhum teste anexa screenshot/log/url)


def pytest_html_results_table_row(report, cells):
    del cells[-1]  # remove coluna "Links" correspondente em cada linha


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["App sob teste"] = "Yodapp (com.qaxperience.yodapp)"
        config._metadata["Automation"] = "UiAutomator2"
        config._metadata["Page Object Model"] = "Sim"


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"
    options.app = APP_PATH
    options.udid = "emulator-5554"
    options.auto_grant_permissions = True

    drv = webdriver.Remote("http://localhost:4723", options=options)
    yield drv
    drv.quit()
