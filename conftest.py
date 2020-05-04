"""Фикстура работы браузера и условия запуска из командной строки"""
import pytest
import logging
from fixtures.browser import Browser


def pytest_addoption(parser):
    """Добавление различных аргументов командной строки"""
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="3", help="waiting time in the seconds", required=False)

@pytest.fixture()
def driver(request):
    """Фикстура запуска различных браузеров"""
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    browser = Browser(browser=browser, wait=wait)
    browser.browser_log.info(f'{browser} is starting!')
    yield browser.driver
    browser.driver.quit()
    browser.browser_log.info(f'{browser} is stopping!')


