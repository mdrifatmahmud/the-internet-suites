from pages.home_page import HomePage
from pages.add_remove_page import AddRemovePage

def test_add_remove_elements(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("Add/Remove Elements")
    page = AddRemovePage(driver, base_url)

    for _ in range(3):
        page.add_element()
    assert page.get_delete_count() == 3

    page.delete_element()
    assert page.get_delete_count() == 2
