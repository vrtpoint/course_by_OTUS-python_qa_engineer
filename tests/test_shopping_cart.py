from resourses.common.base_set_up import BaseSetUp
from resourses.pages.authorization import ApplicationAuthorizationPage
from resourses.pages.shopping_cart import ShoppingCartPage
from decouple import config


class TestShoppingCart(BaseSetUp):

    def test_adding_to_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page._login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCartPage)
        shopping_page._add_to_shopping_cart()
        auth_page._logout()

    def test_removal_position_from_shopping_cart(self):
        self.driver.get(config('url'))
        auth_page = self.get_page(ApplicationAuthorizationPage)
        auth_page._login(config('app_username'), config('app_password'))
        shopping_page = self.get_page(ShoppingCartPage)
        shopping_page._remove_position_from_shopping_cart()
        auth_page._logout()