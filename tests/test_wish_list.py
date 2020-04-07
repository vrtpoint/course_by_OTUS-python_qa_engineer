"""Модуль с тестами списка желаемых покупок"""
from resourses.common.base_set_up import BaseSetUp
from resourses.pages.authorization import ApplicationAuthorizationPage
from resourses.pages.wish_list import WishListPage
from decouple import config


class TestWishList(BaseSetUp):

    def test_adding_to_wish_list(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page._login(config('app_username'), config('app_password'))
        wish_list_page = self.get_page(WishListPage)
        wish_list_page._add_to_wish_list()
        auth_page._logout()

    def test_removal_position_from_wish_list(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page._login(config('app_username'), config('app_password'))
        wish_list_page = self.get_page(WishListPage)
        wish_list_page._remove_from_wish_list()
        auth_page._logout()