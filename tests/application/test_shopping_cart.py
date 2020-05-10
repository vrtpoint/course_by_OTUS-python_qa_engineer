"""Модуль с тестами корзины"""
from resources.common.base_set_up import BaseSetUp
from resources.pages.application.auth import ApplicationAuthorizationPage
from resources.pages.application.shopping_cart import ShoppingCartPage
from decouple import config


class TestShoppingCart(BaseSetUp):

    def test_adding_to_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page.login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCartPage)
        shopping_page.add_to_shopping_cart()
        auth_page.logout(config('app_username'))
        self.check_console(self.driver)

    def test_removal_position_from_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page.login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCartPage)
        shopping_page.remove_position_from_shopping_cart()
        auth_page.logout(config('app_username'))
        self.check_console(self.driver)