from resourses.locators.authorization import AuthorizationLocators
from resourses.locators.wish_list import WishListLocators
from resourses.common.base_actions import BaseActions


class WishListPage(BaseActions):

        wish_list = WishListLocators
        auth = AuthorizationLocators

        def _add_to_wish_list(self):
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

        def _remove_from_wish_list(self):
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