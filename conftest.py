"""Фикстура работы браузера и условия запуска из командной строки"""
import pytest
import logging
from fixtures.browser import Browser


def pytest_addoption(parser):
    """Добавление различных аргументов командной строки"""
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="3", help="waiting time in the seconds", required=False)
    parser.addoption("--file", action='store', default=None, help='file with log report')

@pytest.fixture()
def driver(request):
    """Фикстура запуска различных браузеров"""
    active_browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    filename = request.config.getoption('--file')

    active_browser = Browser(browser=active_browser, wait=wait)
    logging.basicConfig(level=logging.INFO, filename=filename)
    active_browser.browser_log.info(f'{active_browser} is starting!')

    yield active_browser.driver
    active_browser.driver.quit()
    active_browser.browser_log.info(f'{active_browser} is stopping!')


