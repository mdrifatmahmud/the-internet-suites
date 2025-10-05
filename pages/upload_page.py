from selenium.webdriver.common.by import By
from .base_page import BasePage
import os

class UploadPage(BasePage):
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")

    def upload_file(self, filepath):
        self.find(*self.FILE_INPUT).send_keys(os.path.abspath(filepath))
        self.click(*self.SUBMIT)

    def get_uploaded_name(self):
        return self.find(*self.UPLOADED_FILES).text.strip()
