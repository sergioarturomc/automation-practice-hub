from selenium.webdriver.common.by import By
import data


def test_dynamic_table_validation(driver):
    driver.get(data.url)

    # Configurar una espera implícita sencilla para evitar usar WebDriverWait extenso
    driver.implicitly_wait(10)

    # 1. Obtener el texto de CPU de Chrome con un solo XPath directo
    # Busca la fila de Chrome y extrae la celda que tiene el símbolo '%'
    chrome_cpu_element = driver.find_element(
        By.XPATH, "//table[@id='taskTable']//tr[td[1]='Chrome']/td[contains(text(), '%')]"
    )
    val_table = chrome_cpu_element.text.strip()

    # 2. Obtener el valor del párrafo informativo de abajo
    label_element = driver.find_element(
        By.XPATH, "//div[@id='displayValues']//p[contains(text(), 'CPU load of Chrome process')]"
    )
    # Extrae el valor limpiando el texto despues de los dos puntos
    val_label = label_element.text.split(":")[-1].strip()

    # 3. Comparación
    assert val_table == val_label

    ### 4 como el valor cambia  todo el tiempo cada vez que se refresca la pantalla es para validar
    print(val_label)

    ### seria el mismo caso para las demas opciones solo cambiando el selector ya que es dinamica la tabla con algunos valores