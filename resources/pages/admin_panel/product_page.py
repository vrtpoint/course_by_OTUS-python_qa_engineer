"""Модуль с методами для работы с продуктами в панеле администратора"""
from resources.locators.admin_panel.home import SideBar, Products
from resources.common.base_actions import BaseActions


class ProductPage(BaseActions):

        sidebar = SideBar
        product = Products

        def add_product_item(self):
            self._click(*self.sidebar.catalog_list)
            assert self._driver.find_element(*self.sidebar.catalog_list).is_displayed()
            self._click(*self.sidebar.products_link)
            assert self._driver.find_element(*self.sidebar.products_link).is_displayed()
            self._click(*self.product.add_product_item)
            self._input(*self.product.product_name_field, value='тест')
            self._input(*self.product.description_field, value='тест')
            self._input(*self.product.meta_tag_title, value='тест')
            self._click(*self.product.data_link)
            self._input(*self.product.model_field, value='тест')
            self._click(*self.product.submition_button)

        def edit_product_item(self):
            self._click(*self.sidebar.catalog_list)
            self._click(*self.sidebar.products_link)
            self._click(*self.product.add_product_item)[1]