import data
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_scrolling_dropdown(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    print("Probando Scrolling DropDown...")

    # 1. Bajamos la página con la tecla para ver el menú en pantalla
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    # 2. Localizamos el campo desplegable y hacemos clic para abrirlo
    input_dropdown = driver.find_element(By.ID, "comboBox")
    input_dropdown.click()
    time.sleep(1)

    # 3. Mandamos la tecla END para ir hasta el fondo de la lista de golpe
    print("Yendo hasta el final de la lista...")
    input_dropdown.send_keys(Keys.END)
    time.sleep(1)  # Pequeña pausa para que se cargue la vista final

    # 4. Localizamos el "Item 100" y le damos clic
    print("Haciendo clic en el Item 100...")
    item_100 = driver.find_element(By.XPATH, "//div[text()='Item 100']")
    item_100.click()

    time.sleep(3)
    print("¡Prueba de Scrolling DropDown finalizada con éxito!")