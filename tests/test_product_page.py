from locators.product_page import LoginProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def test_authorization(driver, url_param):
    """Тест авторизации пользователя"""
    driver.get(url_param + 'admin')
    driver.find_element(*LoginProductPage.login_field).clear()
    driver.find_element(*LoginProductPage.login_field).send_keys('user')
    driver.find_element(*LoginProductPage.password_field).clear()
    driver.find_element(*LoginProductPage.password_field).send_keys('bitnami1')
    try:
        submit_login_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        submit_login_button.click()
        print('Element is found')
    except TimeoutException:
        print("Element is not found")