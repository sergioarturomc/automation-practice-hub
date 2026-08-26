import data

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_drag_and_drop(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    print("Probando Drag and Drop...")

    # 1. Hacemos scroll hacia abajo para asegurar que el elemento esté en pantalla
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    # 2. Localizamos el origen usando su ID exacto del HTML ("draggable")
    origen = driver.find_element(By.ID, "draggable")

    # 3. Localizamos el destino usando su ID exacto del HTML ("droppable")
    destino = driver.find_element(By.ID, "droppable")

    # 4. Ejecutamos la acción de arrastrar y soltar
    acciones = ActionChains(driver)
    acciones.drag_and_drop(origen, destino).perform()

    # 5. Pausa larga para ver el resultado en el cuadro amarillo
    time.sleep(3)

    print("¡Prueba de Drag and Drop finalizada con éxito!")