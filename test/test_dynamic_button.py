import data
import time

from selenium.webdriver.common.by import By

def test_dynamic_button(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    # 1. Localizar el botón
    boton = driver.find_element(By.XPATH, "//button[contains(@onclick, 'toggleButton')]")

    # --- ESTADO INITIAL (START) ---
    assert boton.text == "START"
    assert boton.get_attribute("class") == "start"

    # 2. Hacer clic para cambiar el estado
    boton.click()

    # --- ESTADO FINAL (STOP) ---
    assert boton.text == "STOP"
    assert boton.get_attribute("class") == "stop"
    assert boton.get_attribute("name") == "stop"

    time.sleep(2)