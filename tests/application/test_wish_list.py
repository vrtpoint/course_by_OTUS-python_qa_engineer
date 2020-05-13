"""Модуль с тестами списка желаемых покупок"""
from resources.common.base_set_up import BaseSetUp
from resources.pages.application.auth import ApplicationAuthorizationPage
from resources.pages.application.wish_list import WishListPage
from decouple import config
import allure

class TestWishList(BaseSetUp):

    @allure.feature('Работа cо списком желаемых покупок')
    def test_adding_to_wish_list(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page.login(config('app_username'), config('app_password'))
        wish_list_page = self.get_page(WishListPage)
        wish_list_page.add_to_wish_list()
        auth_page.logout(config('app_username'))
        self.check_console(self.driver)

    @allure.feature('Работа cо списком желаемых покупок')
    def test_removal_position_from_wish_list(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page.login(config('app_username'), config('app_password'))
        wish_list_page = self.get_page(WishListPage)
        wish_list_page.remove_from_wish_list()
        auth_page.logout(config('app_username'))
        self.check_console(self.driver)