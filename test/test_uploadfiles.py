import time
from pages.automation_form_page import AutomationFormPage
import data



def test_upload_single_file(driver):
    driver.get(data.url)

    form_page = AutomationFormPage(driver)

    form_page.upload_single_file("images.jfif")
    form_page.upload_multiple_files([
        "images.jfif",
        "images (1).jfif",
        "images (2).jfif",
        "images (3).jfif"
    ])

    time.sleep(5)
