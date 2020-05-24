"""Модуль с тестами товарной позиции"""
from resources.common.base_set_up import BaseSetUp
from resources.pages.admin_panel.auth import AdminPanelAuthorizationPage
from resources.pages.admin_panel.product_page import ProductPage
from decouple import config
from fixtures.database import data_base_query
import allure


class TestProducts(BaseSetUp):

    @allure.feature('Работа со списком продуктов')
    def test_addition_product_item(self):
        """Добавление товара в список продуктов"""
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        sidebar = self.get_page(ProductPage)
        sidebar.add_product_item()
        self.check_console(self.driver)
        sql_query = 'SELECT * FROM oc_product WHERE model="test"'
        assert data_base_query(sql_query)

    @allure.feature('Работа со списком продуктов')
    def test_edition_product_item(self):
        """Изменение товара в список желаемых покупок"""
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        product = self.get_page(ProductPage)
        product.edit_button()
        self.check_console(self.driver)
        sql_query = 'SELECT * FROM oc_product WHERE model="test_product"'
        assert data_base_query(sql_query)

    @allure.feature('Работа со списком продуктов')
    def test_deletion_product_item(self):
        """Удаление товара в список желаемых покупок"""
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        product = self.get_page(ProductPage)
        product.delete_product_item()
        self.check_console(self.driver)
        sql_query = 'SELECT * FROM oc_product WHERE model="test_product"'
        assert not data_base_query(sql_query)

    @allure.feature('Работа со списком продуктов')
    def test_uploading_picture(self):
        """Добавление изображения"""
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        product = self.get_page(ProductPage)
        product.upload_picture()
        self.check_console(self.driver)