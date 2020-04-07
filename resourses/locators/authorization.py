from selenium.webdriver.common.by import By


class AuthorizationLocators:

    my_account_link = (By.CSS_SELECTOR, '#top-links .dropdown .fa-user')
    register_link = (By.CSS_SELECTOR, 'ul.dropdown-menu-right li:nth-child(1)')
    login_link = (By.CSS_SELECTOR, 'ul.dropdown-menu-right li:nth-child(2)')
    email_address_field = (By.CSS_SELECTOR, '#input-email')
    password_field = (By.CSS_SELECTOR, '#input-password')
    login_button = (By.CSS_SELECTOR, 'input[type="submit"]')
    logout_button = (By.CSS_SELECTOR, '#top-links .dropdown-menu-right li:nth-child(5) a')
    logout_breadcrumb = (By.CSS_SELECTOR, '.breadcrumb li:nth-child(3)')
    account_breadcrumb = (By.CSS_SELECTOR, '#account-account > ul li:nth-child(2)')
    logo_name = (By.CSS_SELECTOR, '#logo>h1 a')