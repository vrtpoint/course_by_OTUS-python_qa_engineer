from selenium.webdriver.common.by import By


logout_button = (By.CSS_SELECTOR, '.navbar-right .fa-sign-out')

class SideBar:

    catalog_list = (By.CSS_SELECTOR, '#menu-catalog .collapsed')
    products_link = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) a')


class Products:

    products_list = (By.CSS_SELECTOR, '#form-product .table-responsive tr td:nth-child(3)')
    product_item = (By.CSS_SELECTOR, '#form-product .table-responsive tr input[type="checkbox"]')
    add_product_item = (By.CSS_SELECTOR, '.container-fluid .pull-right .btn-primary i')
    edit_product_item = (By.CSS_SELECTOR, '#form-product .table-responsive tr [data-original-title="Edit"]')
    description_field = (By.CSS_SELECTOR, '.note-editor .panel-body')
    submition_button = (By.CSS_SELECTOR, '.pull-right button[type="submit"]')
    delete_product_item = (By.CSS_SELECTOR, '.container-fluid .pull-right .btn-danger')
    operation_status = (By.CSS_SELECTOR, '.alert-success.alert-dismissible')
    product_name_field = (By.CSS_SELECTOR, '#input-name1')
    meta_tag_title = (By.CSS_SELECTOR, '#input-meta-title1')
    data_link = (By.CSS_SELECTOR, '.nav-tabs li:nth-child(2)')
    model_field = (By.CSS_SELECTOR, '#input-model')