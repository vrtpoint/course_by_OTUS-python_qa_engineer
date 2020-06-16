from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from decouple import config

BROWSERSTACK_URL = config('browser_stack_url')

desired_cap = {

    'os': 'OS X',
    'os_version': 'Catalina',
    'browser': 'Firefox',
    'browser_version': '74',
    'name': "virtualpoint1's First Test"

}

driver = webdriver.Remote(
    command_executor=BROWSERSTACK_URL,
    desired_capabilities=desired_cap
)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()
