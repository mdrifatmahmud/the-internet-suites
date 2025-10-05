from pages.home_page import HomePage
from pages.alerts_page import AlertsPage

def test_js_alert(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("JavaScript Alerts")
    page = AlertsPage(driver, base_url)
    page.click_alert()
    driver.switch_to.alert.accept()
    assert "You successfully clicked an alert" in page.get_result()

def test_js_confirm_dismiss(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("JavaScript Alerts")
    page = AlertsPage(driver, base_url)
    page.click_confirm()
    driver.switch_to.alert.dismiss()
    assert "You clicked: Cancel" in page.get_result()
