from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = base_url

    def go(self, path=""):
        url = self.base_url.rstrip("/") + "/" + path.lstrip("/") if self.base_url else path
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        el = self.find(by, locator)
        el.click()
        return el

    def type(self, by, locator, text, clear=True):
        el = self.find(by, locator)
        if clear:
            el.clear()
        el.send_keys(text)
        return el
