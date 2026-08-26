from selenium.webdriver.common.by import By
import data
import time


def test_form_sections(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    # --- SECTION 1 ---
    # Busca la caja de texto justo después del texto 'Section 1'
    input_sec1 = driver.find_element(By.XPATH, "//*[contains(text(),'Section 1')]/following::input[1]")
    input_sec1.send_keys("This is a paragraph in Section 1")

    # Busca el botón 'Submit' correspondiente a la Section 1
    btn_sec1 = driver.find_element(By.XPATH, "//*[contains(text(),'Section 1')]/following::button[1]")
    btn_sec1.click()

    # --- SECTION 2 ---
    input_sec2 = driver.find_element(By.XPATH, "//*[contains(text(),'Section 2')]/following::input[1]")
    input_sec2.send_keys("This is a paragraph in Section 2.")

    btn_sec2 = driver.find_element(By.XPATH, "//*[contains(text(),'Section 2')]/following::button[1]")
    btn_sec2.click()

    # --- SECTION 3 ---
    input_sec3 = driver.find_element(By.XPATH, "//*[contains(text(),'Section 3')]/following::input[1]")
    input_sec3.send_keys("This is a paragraph in Section 3.")

    btn_sec3 = driver.find_element(By.XPATH, "//*[contains(text(),'Section 3')]/following::button[1]")
    btn_sec3.click()

    # --- FOOTER LINKS (Opcional: probar un enlace de abajo) ---
    home_link = driver.find_element(By.LINK_TEXT, "Home")
    # home_link.click()

    time.sleep(2)