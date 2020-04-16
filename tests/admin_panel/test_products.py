"""Модуль с тестами товарной позиции"""
from resources.common.base_set_up import BaseSetUp
from resources.pages.admin_panel.auth import AdminPanelAuthorizationPage
from resources.pages.admin_panel.product_page import ProductPage
from decouple import config


class TestProducts(BaseSetUp):

    def test_addition_product_item(self):
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        sidebar = self.get_page(ProductPage)
        sidebar.add_product_item()

    def test_edition_product_item(self):
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        product = self.get_page(ProductPage)
        product.edit_button()

    def test_deletion_product_item(self):
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        product = self.get_page(ProductPage)
        product.delete_product_item()

    def test_uploading_userpicture(self):
        self.driver.get(config('url') + '/admin')
        auth_page = self.get_page(AdminPanelAuthorizationPage)
        auth_page.login(config('admin_username'), config('admin_password'))
        product = self.get_page(ProductPage)
        product.upload_userpicture()