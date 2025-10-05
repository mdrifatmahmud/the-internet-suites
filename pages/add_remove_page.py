from selenium.webdriver.common.by import By
from .base_page import BasePage

class AddRemovePage(BasePage):
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "button.added-manually")

    def add_element(self):
        self.click(*self.ADD_BUTTON)

    def delete_element(self):
        buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
        if buttons:
            buttons[-1].click()

    def get_delete_count(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))
