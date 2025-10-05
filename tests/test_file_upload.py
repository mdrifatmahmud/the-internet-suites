from pages.home_page import HomePage
from pages.upload_page import UploadPage
from helpers.utils import assets_path

def test_file_upload(driver, base_url):
    home = HomePage(driver, base_url)
    home.go("/")
    home.open_example("File Upload")
    page = UploadPage(driver, base_url)
    page.upload_file(assets_path("upload_test_file.txt"))
    assert "upload_test_file.txt" in page.get_uploaded_name()
