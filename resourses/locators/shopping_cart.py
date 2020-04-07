from selenium.webdriver.common.by import By


class ShoppingCartLocators:

    add_to_cart_button = (By.CSS_SELECTOR, '#content i.fa-shopping-cart')
    cart_link = (By.CSS_SELECTOR, 'a[title="Shopping Cart"]')
    cart_product_name = (By.CSS_SELECTOR, '.table-bordered .text-left > a')
    delete_cart_position_button = (By.CSS_SELECTOR, '.btn.btn-danger .fa-times-circle')
    cart_info = (By.CSS_SELECTOR, '#content h1')