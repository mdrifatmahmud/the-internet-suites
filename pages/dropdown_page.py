from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def select_by_text(self, text):
        el = self.find(*self.DROPDOWN)
        Select(el).select_by_visible_text(text)

    def get_selected(self):
        el = self.find(*self.DROPDOWN)
        return Select(el).first_selected_option.text.strip()
