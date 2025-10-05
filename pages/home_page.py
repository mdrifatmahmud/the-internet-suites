# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    EXAMPLES_LIST = (By.CSS_SELECTOR, "ul li a")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def go(self, path="/"):
        self.driver.get(f"{self.base_url}{path}")

    def open_example(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.EXAMPLES_LIST)
        )
        links = self.driver.find_elements(*self.EXAMPLES_LIST)
        for link in links:
            if link.text.strip().lower() == name.lower():
                link.click()
                return
        raise Exception(f"Example '{name}' not found on homepage")
