from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging


# Класс для работа с событиями в браузере
class BrowserListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        logging.error(f'{exception}')
        self.driver.save_screenshot(f'screenshots/{exception}.png')


class Browser:

    def __init__(self, browser, wait):
        if browser == "chrome":
            self.driver = EventFiringWebDriver(webdriver.Chrome(), BrowserListener())
        elif browser == "firefox":
            self.driver = EventFiringWebDriver(webdriver.Firefox(), BrowserListener())
        elif browser == "opera":
            self.driver = EventFiringWebDriver(webdriver.Opera(), BrowserListener())
        elif browser == "safari":
            self.driver = EventFiringWebDriver(webdriver.Safari(), BrowserListener())
        else:
            raise Exception(f"{request.param} is not supported!")

        self.driver.maximize_window()
        self.driver.implicitly_wait(wait)



