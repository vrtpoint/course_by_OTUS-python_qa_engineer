"""Модуль с методами для авторизации"""
from resources.locators.application.auth import AuthorizationLocators
from resources.common.base_actions import BaseActions


class ApplicationAuthorizationPage(BaseActions):

        LOGGER_NAME = 'ApplicationAuthorizationPage'

        auth = AuthorizationLocators

        def __index__(self, driver):
            super().__init__(driver, self.LOGGER_NAME)

        def login(self, app_username, app_password):
            self._click(*self.auth.my_account_link)
            self._click(*self.auth.login_link)
            self._input(*self.auth.email_address_field, value=app_username)
            self._input(*self.auth.password_field, value=app_password)
            self._click(*self.auth.login_button)

            assert self._driver\
                .find_element(*self.auth.account_breadcrumb).text == 'Account'
            self.logger.info(f'{app_username} was logged in')

        def logout(self, app_username):
            self._click(*self.auth.my_account_link)
            self._click(*self.auth.logout_button)

            assert self._driver \
                .find_element(*self.auth.logout_breadcrumb).text == 'Logout'
            self.logger.info(f'{app_username} was logged out')