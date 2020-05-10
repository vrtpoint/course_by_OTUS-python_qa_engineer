"""Модуль с методами работы драйвера"""
import pytest


class BaseSetUp:

    @pytest.fixture(autouse=True)
    def set_up_driver(self, driver):
        self.driver = driver
        yield self.driver

    def get_page(self, Page):
        return Page(self.driver)

    def check_console(self, driver):
        """Метод проверки корректности логов"""
        self.driver = driver
        for log in self.driver.get_log('browser'):
            assert 'Uncaught' not in log