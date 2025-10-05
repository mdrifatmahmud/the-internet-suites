import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from helpers.utils import load_test_data

data = load_test_data()

def test_valid_login(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("Form Authentication")
    page = LoginPage(driver, base_url)
    page.login(data["valid_user"]["username"], data["valid_user"]["password"])
    assert "You logged into a secure area!" in page.get_flash_text()

def test_invalid_login(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("Form Authentication")
    page = LoginPage(driver, base_url)
    page.login(data["invalid_user"]["username"], data["invalid_user"]["password"])
    assert "Your username is invalid!" in page.get_flash_text()
