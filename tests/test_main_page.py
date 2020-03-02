"""Тесты главной страницы opencart"""
from locators.main_page import MainPage


def test_login_user(driver, url_param):
    """Тест авторизации пользователя"""
    driver.get(url_param)
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.login_link).click()
    driver.find_element(*MainPage.HeaderSection.email_address_field).clear()
    driver.find_element(*MainPage.HeaderSection.email_address_field).send_keys('t@t.t')
    driver.find_element(*MainPage.HeaderSection.password_field).clear()
    driver.find_element(*MainPage.HeaderSection.password_field).send_keys('test123')
    driver.find_element(*MainPage.HeaderSection.login_button).click()
    assert driver.find_element(*MainPage.InnerSection.account_breadcrumb).text == 'Account'
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.logout_button).click()
    assert driver.find_element(*MainPage.InnerSection.logout_breadcrumb).text == 'Logout'


def test_adding_to_wish_list(driver, url_param):
    """Тест добавления позиции в список желаемых покупок"""
    driver.get(url_param)
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.login_link).click()
    driver.find_element(*MainPage.HeaderSection.email_address_field).clear()
    driver.find_element(*MainPage.HeaderSection.email_address_field).send_keys('t@t.t')
    driver.find_element(*MainPage.HeaderSection.password_field).clear()
    driver.find_element(*MainPage.HeaderSection.password_field).send_keys('test123')
    driver.find_element(*MainPage.HeaderSection.login_button).click()
    driver.find_element(*MainPage.HeaderSection.logo_name).click()
    assert driver.find_element(*MainPage.MainSection.slide_section).is_displayed()
    feature_elements = driver.find_elements(*MainPage.MainSection.featured_section)
    product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']
    for element in feature_elements:
        assert element.text in product_list
        print(element.text)
    feature_element = driver.find_elements(*MainPage.MainSection.featured_section)[0]
    feature_element.click()
    driver.find_element(*MainPage.MainSection.wish_list_button).click()
    driver.find_element(*MainPage.HeaderSection.wish_list_link).click()
    assert driver.find_element(*MainPage.MainSection.wish_list_product_name).text == 'MacBook'
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.logout_button).click()
    assert driver.find_element(*MainPage.InnerSection.logout_breadcrumb).text == 'Logout'


def test_removal_position_from_wish_list(driver, url_param):
    """Тест удаления позиции из списка желаемых покупок"""
    driver.get(url_param)
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.login_link).click()
    driver.find_element(*MainPage.HeaderSection.email_address_field).clear()
    driver.find_element(*MainPage.HeaderSection.email_address_field).send_keys('t@t.t')
    driver.find_element(*MainPage.HeaderSection.password_field).clear()
    driver.find_element(*MainPage.HeaderSection.password_field).send_keys('test123')
    driver.find_element(*MainPage.HeaderSection.login_button).click()
    driver.find_element(*MainPage.HeaderSection.logo_name).click()
    assert driver.find_element(*MainPage.MainSection.slide_section).is_displayed()
    feature_elements = driver.find_elements(*MainPage.MainSection.featured_section)
    product_list = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']
    for element in feature_elements:
        assert element.text in product_list
        print(element.text)
    feature_element = driver.find_elements(*MainPage.MainSection.featured_section)[0]
    feature_element.click()
    driver.find_element(*MainPage.HeaderSection.wish_list_link).click()
    driver.find_element(*MainPage.InnerSection.delete_wish_list_position_button).click()
    assert driver.find_element(*MainPage.InnerSection.my_wish_list_breadcrumb).text == 'My Wish List'
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.logout_button).click()
    assert driver.find_element(*MainPage.InnerSection.logout_breadcrumb).text == 'Logout'


def test_adding_to_shopping_cart(driver, url_param):
    """Тест добавления позиции в корзину покупок"""
    driver.get(url_param)
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.login_link).click()
    driver.find_element(*MainPage.HeaderSection.email_address_field).clear()
    driver.find_element(*MainPage.HeaderSection.email_address_field).send_keys('t@t.t')
    driver.find_element(*MainPage.HeaderSection.password_field).clear()
    driver.find_element(*MainPage.HeaderSection.password_field).send_keys('test123')
    driver.find_element(*MainPage.HeaderSection.login_button).click()
    driver.find_element(*MainPage.HeaderSection.logo_name).click()
    assert driver.find_element(*MainPage.MainSection.slide_section).is_displayed()
    cart_buttons = driver.find_elements(*MainPage.MainSection.add_to_cart_button)
    for element in cart_buttons:
        assert element is not None
    cart_button = driver.find_elements(*MainPage.MainSection.add_to_cart_button)[0]
    cart_button.click()
    driver.find_element(*MainPage.HeaderSection.shopping_cart_link).click()
    assert driver.find_element(*MainPage.MainSection.shopping_cart_product_name).text == 'MacBook'
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.logout_button).click()
    assert driver.find_element(*MainPage.InnerSection.logout_breadcrumb).text == 'Logout'


def test_removal_position_from_shopping_cart(driver, url_param):
    """Тест удаления позиции из корзины покупок"""
    driver.get(url_param)
    driver.find_element(*MainPage.HeaderSection.my_account_link).click()
    driver.find_element(*MainPage.HeaderSection.login_link).click()
    driver.find_element(*MainPage.HeaderSection.email_address_field).clear()
    driver.find_element(*MainPage.HeaderSection.email_address_field).send_keys('t@t.t')
    driver.find_element(*MainPage.HeaderSection.password_field).clear()
    driver.find_element(*MainPage.HeaderSection.password_field).send_keys('test123')
    driver.find_element(*MainPage.HeaderSection.login_button).click()
    driver.find_element(*MainPage.HeaderSection.logo_name).click()
    driver.find_element(*MainPage.HeaderSection.shopping_cart_link).click()
    driver.find_element(*MainPage.InnerSection.delete_shopping_cart_position_button).click()
    assert driver.find_element(*MainPage.InnerSection.shopping_cart_info).text == 'Shopping Cart'