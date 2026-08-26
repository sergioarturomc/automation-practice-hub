import data

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_slider(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    print("Probando Slider...")

    # 1. Bajamos la página con la tecla para ver el slider en pantalla
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    # 2. Localizamos los dos tiradores usando su clase exacta que vimos en el HTML
    sliders = driver.find_elements(By.XPATH, "//span[contains(@class, 'ui-slider-handle')]")

    slider_izquierdo = sliders[0]
    slider_derecho = sliders[1]

    acciones = ActionChains(driver)

    # 3. Mover el slider izquierdo (lo arrastramos hacia la izquierda por seguridad con un valor negativo)
    print("Moviendo slider izquierdo...")
    acciones.drag_and_drop_by_offset(slider_izquierdo, -50, 0).perform()
    time.sleep(2)

    # 4. Mover el slider derecho hacia la derecha (ejemplo: 100 píxeles para asegurarnos de llevarlo al 100%)
    print("Moviendo slider derecho...")
    acciones.drag_and_drop_by_offset(slider_derecho, 100, 0).perform()
    time.sleep(2)

    print("¡Prueba de Slider finalizada con éxito!")