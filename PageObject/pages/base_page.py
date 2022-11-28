from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicity_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
