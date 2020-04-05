"""Фикстура работы браузера и условия запуска из командной строки"""
from selenium import webdriver
import pytest

# Добавление различных аргументов командной строки
def pytest_addoption(parser):
    parser.addoption("--opencart_url", action="store", default="http://localhost/", help="This is opencart_url", required=False)
    parser.addoption("--browser", action="store", default="firefox", help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="3", help="waiting time in the seconds", required=False)

# Фикстура запуска различных браузеров
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.maximize_window()
    driver.implicitly_wait(wait)
    request.addfinalizer(driver.close)


    return driver

@pytest.fixture()
def url_param(request):
    """Фикстура возвращает аргумент выбора url командной строки"""
    return request.config.getoption("--opencart_url")