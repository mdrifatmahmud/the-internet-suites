from pages.home_page import HomePage
from pages.dropdown_page import DropdownPage

def test_dropdown_select(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("Dropdown")
    page = DropdownPage(driver, base_url)
    page.select_by_text("Option 2")
    assert page.get_selected() == "Option 2"
