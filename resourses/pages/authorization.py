"""Модуль с методами для авторизации"""
from resourses.locators.authorization import AuthorizationLocators
from resourses.common.base_actions import BaseActions


class ApplicationAuthorizationPage(BaseActions):

        auth = AuthorizationLocators

        def _login(self, app_username, app_password):
            self._click(*self.auth.my_account_link)
            self._click(*self.auth.login_link)
            self._input(*self.auth.email_address_field, value=app_username)
            self._input(*self.auth.password_field, value=app_password)
            self._click(*self.auth.login_button)

            assert self._driver\
                .find_element(*self.auth.account_breadcrumb).text == 'Account'

        def _logout(self):
            self._click(*self.auth.my_account_link)
            self._click(*self.auth.logout_button)

            assert self._driver \
               .find_element(*self.auth.logout_breadcrumb).text == 'Logout'