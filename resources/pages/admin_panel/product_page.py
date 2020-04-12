"""Модуль с методами для работы с продуктами в панеле администратора"""
from selenium.webdriver.common.alert import Alert
from resources.locators.admin_panel.home import SideBar, Products
from resources.common.base_actions import BaseActions


class ProductPage(BaseActions):

        sidebar = SideBar
        product = Products

        def add_product_item(self):
            self._click(*self.sidebar.catalog_list)
            self._click(*self.sidebar.products_link)
            self._click(*self.product.add_product_item)
            self._input(*self.product.product_name_field, value='test')
            self._input(*self.product.description_field, value='test')
            self._input(*self.product.meta_tag_title, value='test')
            self._click(*self.product.data_link)
            self._input(*self.product.model_field, value='test')
            self._click(*self.product.submition_button)
            assert self._driver.find_element(*self.product.operation_status).text.split("\n")[0] == 'Success: You have modified products!'

        def edit_product_item(self):
            self._click(*self.sidebar.catalog_list)
            self._click(*self.sidebar.products_link)
            concrete_product = self._driver.find_elements(*self.product.product_item)[19]
            concrete_product.click()
            edit_element = self._driver.find_elements(*self.product.edit_product_item)[18]
            edit_element.click()
            self._input(*self.product.product_name_field, value='test_product')
            self._input(*self.product.description_field, value='test_product')
            self._click(*self.product.submition_button)
            assert self._driver.find_element(*self.product.operation_status).text.split("\n")[0] == 'Success: You have modified products!'

        def delete_product_item(self):
            self._click(*self.sidebar.catalog_list)
            self._click(*self.sidebar.products_link)
            concrete_product = self._driver.find_elements(*self.product.product_item)[19]
            concrete_product.click()
            self._click(*self.product.delete_product_item)
            Alert(self._driver).accept()
            assert self._driver.find_element(*self.product.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
