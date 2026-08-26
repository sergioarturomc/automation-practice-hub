import time
from selenium.webdriver.common.by import By
import data



def test_alerts_and_popups_slow(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    # 1. SIMPLE ALERT (Alerta normal de aceptar)
    print("Probando Simple Alert")
    driver.find_element(By.XPATH, "//button[text()='Simple Alert']").click()
    time.sleep(2)

    alerta = driver.switch_to.alert
    alerta.accept()  # Clic en OK
    time.sleep(1)

    # 2. CONFIRMATION ALERT (Aceptar o Cancelar)
    print("Probando Confirmation Alert")
    driver.find_element(By.XPATH, "//button[text()='Confirmation Alert']").click()
    time.sleep(2)

    driver.switch_to.alert.dismiss()  # Clic en Cancelar
    time.sleep(1)

    # 3. PROMPT ALERT (Escribir texto y aceptar)
    print("Probando Prompt Alert")
    driver.find_element(By.XPATH, "//button[text()='Prompt Alert']").click()
    time.sleep(2)

    prompt = driver.switch_to.alert
    prompt.send_keys("Hola Sergio")  # Escribimos texto
    time.sleep(2)
    prompt.accept()
    time.sleep(1)

    # 4. NEW TAB (Nueva Pestaña - Versión Simple)
    print("Probando New Tab")
    driver.find_element(By.XPATH, "//button[text()='New Tab']").click()
    time.sleep(2)

    # Cambiar a la nueva pestaña (que está en la posición 1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    driver.close()  # Cerramos la pestaña nueva

    # Regresar a la ventana principal (que está en la posición 0)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    # 5. POPUP WINDOWS (Ventana emergente - Versión Simple)
    print("Probando Popup Windows")
    driver.find_element(By.XPATH, "//button[text()='Popup Windows']").click()
    time.sleep(2)

    # Cambiar a la ventana emergente (posición 1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    driver.close()  # Cerramos la ventana emergente

    # Regresar a la ventana principal (posición 0)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)