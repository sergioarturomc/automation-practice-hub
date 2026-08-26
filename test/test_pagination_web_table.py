
import data
from selenium.webdriver.common.by import By

def test_pagination_checkboxes(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    # --- PÁGINA 1 ---
    # 1. Traer y hacer clic en los checkboxes de la tabla 1
    checkboxes = driver.find_elements(By.XPATH, "//table[@id='productTable']//input[@type='checkbox']")
    for chk in checkboxes:
        chk.click()

    # --- PÁGINA 2 ---
    driver.find_element(By.LINK_TEXT, "2").click()
    checkboxes = driver.find_elements(By.XPATH, "//table[@id='productTable']//input[@type='checkbox']")
    for chk in checkboxes:
        chk.click()

    # --- PÁGINA 3 ---
    driver.find_element(By.LINK_TEXT, "3").click()
    checkboxes = driver.find_elements(By.XPATH, "//table[@id='productTable']//input[@type='checkbox']")
    for chk in checkboxes:
        chk.click()

    # --- PÁGINA 4 ---
    driver.find_element(By.LINK_TEXT, "4").click()
    checkboxes = driver.find_elements(By.XPATH, "//table[@id='productTable']//input[@type='checkbox']")
    for chk in checkboxes:
        chk.click()
