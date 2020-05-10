"""Модуль с методами действий на сайте"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fixtures.logger import browser_log


class BaseActions:

    LOGGER_NAME = 'base'

    def __init__(self, driver):
        self.logger = browser_log(self.LOGGER_NAME)
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 30)

    def __searching_element(self, type_selector, selector):
        try:
            self.__wait.until(EC.presence_of_element_located((type_selector, selector)))
            self.__wait.until(EC.element_to_be_clickable((type_selector, selector)))
        except:
            raise self.logger.error(Exception(f'Element {(type_selector, selector)} is not found!'))
        self.logger.info(f'Element {(type_selector, selector)} is searchable')
        return self._driver.find_element(type_selector, selector)

    def _click(self, type_selector, selector):
        try:
            self.__searching_element(type_selector, selector).click()
        except:
            raise self.logger.error(Exception(f'Element {(type_selector, selector)} is not clickable!'))
        self.logger.info(f'element {(type_selector, selector)} is clickable')

    def _input(self, type_selector, selector, value):
        try:
            self.__searching_element(type_selector, selector).clear()
            self.__searching_element(type_selector, selector).send_keys(value)
        except:
            raise self.logger.error(Exception(f'Element {(type_selector, selector)} is not inputable!'))
        self.logger.info(f'element {(type_selector, selector)} is inputable')

