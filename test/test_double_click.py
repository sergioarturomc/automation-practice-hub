import data

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_double_click_simple(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    print("Probando Double Click")

    # OPCIÓN FÁCIL: En lugar de JavaScript, le mandamos una orden
    # al cuerpo de la página para que baje un poco con la tecla "AvPág" (Page Down)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Pausa para ver cómo bajó la pantalla

    # 2. Localizamos el botón "Copy Text"
    boton_copy = driver.find_element(By.XPATH, "//button[text()='Copy Text']")

    # 3. Hacemos el doble clic con ActionChains (que ya conoces)
    acciones = ActionChains(driver)
    acciones.double_click(boton_copy).perform()

    # 4. Pausa para ver el resultado en Field2
    time.sleep(3)

    print("¡Prueba de Double Click finalizada con éxito!")