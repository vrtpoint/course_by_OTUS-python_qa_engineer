from selenium.webdriver.common.alert import Alert
from locators.product_page import LoginProductPage, AdminPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def test_addition_product_item(driver, url_param):
    """Тест добавления выбранного товара"""
    driver.get(url_param + 'admin')
    driver.find_element(*LoginProductPage.login_field).clear()
    driver.find_element(*LoginProductPage.login_field).send_keys('user')
    driver.find_element(*LoginProductPage.password_field).clear()
    driver.find_element(*LoginProductPage.password_field).send_keys('bitnami1')
    driver.find_element(*LoginProductPage.submit_login_button).click()
    driver.find_element(*AdminPage.catalog_list).click()
    driver.find_element(*AdminPage.products_link).click()
    driver.find_element(*AdminPage.Products.add_product_item).click()
    driver.find_element(*AdminPage.Products.product_name_field).send_keys('What is Lorem Ipsum?')
    driver.find_element(*AdminPage.Products.meta_tag_title).send_keys('What is Lorem Ipsum?')
    driver.find_element(*AdminPage.Products.data_link).click()
    driver.find_element(*AdminPage.Products.model_field).clear()
    driver.find_element(*AdminPage.Products.model_field).send_keys('Product 1')
    try:
        submition_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'У.pull-right button[type="submit"]')))
        submition_button.click()
        print('Element is found')
    except TimeoutException:
        print("Element is not found")
    assert driver.find_element(*AdminPage.Products.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
    driver.find_element(*AdminPage.logout_button).click()
    assert driver.find_element(*LoginProductPage.entry_title).text == 'Please enter your login details.'

def test_edition_product_item(driver, url_param):
    """Тест изменения выбранного товара"""
    driver.get(url_param + 'admin')
    driver.find_element(*LoginProductPage.login_field).clear()
    driver.find_element(*LoginProductPage.login_field).send_keys('user')
    driver.find_element(*LoginProductPage.password_field).clear()
    driver.find_element(*LoginProductPage.password_field).send_keys('bitnami1')
    driver.find_element(*LoginProductPage.submit_login_button).click()
    driver.find_element(*AdminPage.catalog_list).click()
    try:
        products_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) a')))
        products_link.click()
        print('Element is found')
    except TimeoutException:
        print("Element is not found")
    concrete_product = driver.find_elements(*AdminPage.Products.product_item)[1]
    concrete_product.click()
    edit_concrete_product = driver.find_elements(*AdminPage.Products.edit_product_item)[0]
    edit_concrete_product.click()
    driver.find_element(*AdminPage.Products.description_field).clear()
    driver.find_element(*AdminPage.Products.description_field).send_keys('The Apple 30-Inch Cinema Display (Aluminum)')
    driver.find_element(*AdminPage.Products.submition_button).click()
    assert driver.find_element(*AdminPage.Products.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
    driver.find_element(*AdminPage.logout_button).click()
    assert driver.find_element(*LoginProductPage.entry_title).text == 'Please enter your login details.'

def test_deletion_product_item(driver, url_param):
    """Тест удаления выбранного товара"""
    driver.get(url_param + 'admin')
    driver.find_element(*LoginProductPage.login_field).clear()
    driver.find_element(*LoginProductPage.login_field).send_keys('user')
    driver.find_element(*LoginProductPage.password_field).clear()
    driver.find_element(*LoginProductPage.password_field).send_keys('bitnami1')
    driver.find_element(*LoginProductPage.submit_login_button).click()
    try:
        catalog_list = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#menu-catalog .collapsed')))
        catalog_list.click()
        print('Element is found')
    except TimeoutException:
        print("Element is not found")
    driver.find_element(*AdminPage.products_link).click()
    concrete_product = driver.find_elements(*AdminPage.Products.product_item)[1]
    concrete_product.click()
    driver.find_element(*AdminPage.Products.delete_product_item).click()
    Alert(driver).accept()
    time.sleep(2)
    assert driver.find_element(*AdminPage.Products.operation_status).text.split("\n")[0] == 'Success: You have modified products!'
    driver.find_element(*AdminPage.logout_button).click()
    assert driver.find_element(*LoginProductPage.entry_title).text == 'Please enter your login details.'