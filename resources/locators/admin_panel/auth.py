from selenium.webdriver.common.by import By


class LoginProductPage:

    login_field = (By.CSS_SELECTOR, '#input-username')
    password_field = (By.CSS_SELECTOR, '#input-password')
    submit_login_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    entry_title = (By.CSS_SELECTOR, '.panel-title')
