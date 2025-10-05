import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# -------------------------
# Load config from config.json
# -------------------------
def load_config():
    with open("config.json") as f:
        return json.load(f)


# -------------------------
# Base URL Fixture
# -------------------------
@pytest.fixture(scope="session")
def base_url():
    config = load_config()
    return config["base_url"]


# -------------------------
# WebDriver Fixture
# -------------------------
@pytest.fixture(scope="function")
def driver():
    config = load_config()
    opts = Options()
    opts.add_argument(f"--window-size={config['window_size']}")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    driver.implicitly_wait(config["implicit_wait"])
    yield driver
    driver.quit()
