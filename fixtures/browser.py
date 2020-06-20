from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
from .logger import browser_log


class BrowserListener(AbstractEventListener):
    """Класс для работа с событиями в браузере"""

    def on_exception(self, exception, driver):
        """Метод снятия скриншота при возникновении ошибки"""
        logging.error(f'{exception}')
        driver.save_screenshot(f'screenshots/{exception}.png')


class Browser:
    """Класс для работа с настройками браузеров"""

    LOGGER_NAME = 'browser'

    def __init__(self, browser, wait, selenoid):

        capabilities = {
            "browserName": "chrome",
            "version": "83.0",
        }
        if selenoid == True:
            driver = webdriver.Remote(command_executor=f"http://localhost:8082/wd/hub",
                                      desired_capabilities=capabilities)
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            self.driver = EventFiringWebDriver(webdriver.Chrome(options=options), BrowserListener())
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
        self.browser_log = browser_log(self.LOGGER_NAME)



