"""Фикстура работы браузера и условия запуска из командной строки"""
from selenium import webdriver
import pytest
import logging
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


# Добавление различных аргументов командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="3", help="waiting time in the seconds", required=False)


# Класс для работа с событиями в браузере
class BrowserListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        logging.error(f'{exception}')
        driver.save_screenshot(f'screenshots/{exception}.png')


# Фикстура запуска различных браузеров
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    if browser == "chrome":
        driver = EventFiringWebDriver(webdriver.Chrome(), BrowserListener())
    elif browser == "firefox":
        driver = EventFiringWebDriver(webdriver.Firefox(), BrowserListener())
    elif browser == "opera":
        driver = EventFiringWebDriver(webdriver.Opera(), BrowserListener())
    elif browser == "safari":
        driver = EventFiringWebDriver(webdriver.Safari(), BrowserListener())
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.maximize_window()
    driver.implicitly_wait(wait)

    request.addfinalizer(driver.close)

    return driver


