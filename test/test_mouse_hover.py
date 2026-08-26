import data
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_mouse_hover(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    print("Probando Mouse Hover")

    # 1. Localizamos el botón principal "Point Me"
    boton_point_me = driver.find_element(By.XPATH, "//button[text()='Point Me']")

    # 2. ¡NUEVO! Hacemos scroll hacia abajo para que el botón quede visible en el centro de tu pantalla
    driver.execute_script("arguments[0].scrollIntoView(true);", boton_point_me)
    time.sleep(1)  # Pausa para ver cómo se desliza la página

    # 3. Creamos la acción para pasar el mouse por encima
    acciones = ActionChains(driver)
    acciones.move_to_element(boton_point_me).perform()

    # Pausa más larga para que aprecies claramente cómo se despliega el menú
    time.sleep(3)

    # 4. Hacemos clic en la primera opción: "Mobiles"
    print("Haciendo clic en Mobiles")
    opcion_mobiles = driver.find_element(By.XPATH, "//a[text()='Mobiles']")
    opcion_mobiles.click()
    time.sleep(2)

    # 5. Volvemos a hacer scroll por si la página se movió
    driver.execute_script("arguments[0].scrollIntoView(true);", boton_point_me)
    time.sleep(1)

    # 6. Volvemos a pasar el mouse por encima de "Point Me"
    acciones.move_to_element(boton_point_me).perform()
    time.sleep(2)  # Pausa para ver el menú abierto de nuevo

    # 7. Hacemos clic en la segunda opción: "Laptops"
    print("Haciendo clic en Laptops")
    opcion_laptops = driver.find_element(By.XPATH, "//a[text()='Laptops']")
    opcion_laptops.click()
    time.sleep(3)

    print("¡Prueba de Mouse Hover finalizada con éxito!")