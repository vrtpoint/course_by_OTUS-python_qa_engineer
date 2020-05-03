"""Фикстура работы браузера и условия запуска из командной строки"""
import pytest
from fixtures.browser import Browser


# Добавление различных аргументов командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="3", help="waiting time in the seconds", required=False)


#Фикстура запуска различных браузеров
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    browser = Browser(browser=browser, wait=wait)

    request.addfinalizer(browser.driver.close)
    return browser.driver



