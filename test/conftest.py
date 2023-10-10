import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
appium_server_url = 'http://localhost:4723'
# Crie uma instância de Options
options = AppiumOptions()
options.set_capability('platformName', 'Android')
options.set_capability('automationName', 'Flutter')
options.set_capability('deviceName', 'emulator-5554')
options.set_capability('app', '../magnum-bank-app-flutter/build/app/outputs/flutter-apk/app-dev-profile.apk')
options.set_capability('appPackage', 'br.com.magnumbank.dev')


    

@pytest.fixture(scope="class")
def driver_setup(request):
    driver = webdriver.Remote(appium_server_url, options=options)
    request.cls.driver = driver  # Adicionar driver como um atributo da classe
    yield driver
    driver.quit()

