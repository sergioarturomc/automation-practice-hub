import data


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_verify_svg_elements_present(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    print("Verificando la presencia de los elementos SVG")

    # 1. Bajamos la página para que los elementos sean visibles en pantalla
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    # 2. Localizamos y validamos el Círculo Rojo
    circulo_rojo = driver.find_element(By.XPATH, "//*[local-name()='circle' and @fill='red']")
    assert circulo_rojo.is_displayed(), "¡El círculo rojo no está visible!"
    print("✓ Círculo rojo presente y visible.")

    # 3. Localizamos y validamos el Rectángulo Verde
    rectangulo_verde = driver.find_element(By.XPATH, "//*[local-name()='rect' and @fill='green']")
    assert rectangulo_verde.is_displayed(), "¡El rectángulo verde no está visible!"
    print("✓ Rectángulo verde presente y visible.")

    # 4. Localizamos y validamos el Triángulo Azul
    triangulo_azul = driver.find_element(By.XPATH, "//*[local-name()='polygon' and @fill='blue']")
    assert triangulo_azul.is_displayed(), "¡El triángulo azul no está visible!"
    print("✓ Triángulo azul presente y visible.")

    time.sleep(2)
    print("¡Todas las validaciones de presencia SVG finalizaron con éxito!")