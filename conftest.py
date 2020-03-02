"""Фикстура работы браузера и условия запуска из командной строки"""
from selenium import webdriver
import pytest

# Добавление различных аргументов командной строки
def pytest_addoption(parser):
    parser.addoption("--opencart_url", action="store", default="http://localhost/", help="This is opencart_url", required=False)
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--headless", action="store", default=False, help="This is headless mode")

# Фикстура запуска различных браузеров в обычном и headless режимах
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser == 'chrome':
        if headless == False:
            wd = webdriver.Chrome()
            yield wd
            wd.quit()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            wd = webdriver.Chrome(options=options)
            yield wd
            wd.quit()
    elif browser == 'firefox':
        if headless == False:
            wd = webdriver.Firefox()
            yield wd
            wd.quit()
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            wd = webdriver.Firefox(options=options)
            yield wd
            wd.quit()
    elif browser == 'opera':
        wd = webdriver.Opera()
        yield wd
        wd.quit()

# Фикстура возвращает аргумент выбора url командной строки
@pytest.fixture()
def url_param(request):
    return request.config.getoption("--opencart_url")