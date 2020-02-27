# Тест открытия главной страницы opencart
def test_open_page(driver, url_param):
    driver.get(url_param)
    assert driver.title == 'Your Store'
    print('тест пройден')
    driver.close()