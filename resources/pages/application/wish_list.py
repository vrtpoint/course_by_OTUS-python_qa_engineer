"""Модуль с методами для работы со списком желаемых покупок"""
from resources.locators.application.auth import AuthorizationLocators
from resources.locators.application.wish_list import WishListLocators
from resources.common.base_actions import BaseActions


class WishListPage(BaseActions):

        LOGGER_NAME = 'WishListPage'

        wish_list = WishListLocators
        auth = AuthorizationLocators

        def __index__(self, driver):
            super().__init__(driver, self.LOGGER_NAME)

        def add_to_wish_list(self):
            self._click(*self.auth.logo_name)
            assert self._driver.find_element(*self.auth.logo_name).is_displayed()
            feature_elements = self._driver.find_elements(*self.wish_list.featured_section)
            product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']

            for element in feature_elements:
                assert element.text in product_list
                print(element.text)

            feature_element = self._driver.find_elements(*self.wish_list.featured_section)[0]
            feature_element.click()
            self._click(*self.wish_list.wish_list_button)
            self._click(*self.wish_list.wish_list_link)
            assert self._driver \
                .find_element(*self.wish_list.wish_list_product_name) \
                .text == 'MacBook'
            self.logger.info('position was added into wish list')

        def remove_from_wish_list(self):
            self._click(*self.auth.logo_name)
            assert self._driver.find_element(*self.auth.logo_name).is_displayed()
            feature_elements = self._driver.find_elements(*self.wish_list.featured_section)
            product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']

            for element in feature_elements:
                assert element.text in product_list
                print(element.text)

            feature_element = self._driver.find_elements(*self.wish_list.featured_section)[0]
            feature_element.click()
            self._click(*self.wish_list.wish_list_link)
            self._click(*self.wish_list.delete_wish_list_position_button)
            assert self._driver \
                .find_element(*self.wish_list.my_wish_list_breadcrumb) \
                .text == 'My Wish List'
            self.logger.info('position was added into wish list')