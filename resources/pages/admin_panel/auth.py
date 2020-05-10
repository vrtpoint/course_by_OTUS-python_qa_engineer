from resources.locators.admin_panel.auth import LoginProductPage
from resources.locators.admin_panel.home import Menu
from resources.common.base_actions import BaseActions


class AdminPanelAuthorizationPage(BaseActions):

        LOGGER_NAME = 'AdminPanelAuthorizationPage'

        auth = LoginProductPage
        menu = Menu

        def __index__(self, driver):
            super().__init__(driver, self.LOGGER_NAME)

        def login(self, app_username, app_password):
            self._input(*self.auth.login_field, value=app_username)
            self._input(*self.auth.password_field, value=app_password)
            self._click(*self.auth.submit_login_button)

            assert self._driver \
                       .find_element(*self.menu.dashboard_title).text == 'Dashboard'
            self.logger.info(f'{app_username} was logged in')