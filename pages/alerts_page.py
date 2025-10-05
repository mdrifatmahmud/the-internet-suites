from selenium.webdriver.common.by import By
from .base_page import BasePage

class AlertsPage(BasePage):
    JS_ALERT = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT = (By.ID, "result")

    def click_alert(self):
        self.click(*self.JS_ALERT)

    def click_confirm(self):
        self.click(*self.JS_CONFIRM)

    def click_prompt(self):
        self.click(*self.JS_PROMPT)

    def get_result(self):
        return self.find(*self.RESULT).text.strip()
