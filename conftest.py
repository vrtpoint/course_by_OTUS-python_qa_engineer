"""Фикстура работы браузера и условия запуска из командной строки"""
from selenium import webdriver
import pytest


# Добавление различных аргументов командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "safari", "opera"])
    parser.addoption("--executor", action="store", default="192.168.1.44")
    parser.addoption("--implicitly_wait", action="store", default="3",
                     help="waiting time in the seconds", required=False)
    parser.addoption("--selenoid", action="store", default="192.168.1.44")


# Фикстура запуска удаленного запуска браузера
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    selenoid = request.config.getoption("--selenoid")
    executor = request.config.getoption("--executor")

    capabilities = {
        "browserName": "chrome",
        "version": "68.0",
        #"enableVNC": True,
        #"enableVideo": False
    }
    if selenoid:
        executor = "192.168.1.37"
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities=capabilities)
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

