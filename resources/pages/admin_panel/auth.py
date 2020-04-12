from resources.locators.admin_panel.auth import LoginProductPage
from resources.common.base_actions import BaseActions


class AdminPanelAuthorizationPage(BaseActions):

        auth = LoginProductPage

        def login(self, app_username, app_password):
            self._input(*self.auth.login_field, value=app_username)
            self._input(*self.auth.password_field, value=app_password)
            self._click(*self.auth.submit_login_button)