import data
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_tabs_interaction(driver):
    driver.get(data.url)
    driver.implicitly_wait(5)

    # 1. Clic en el título usando la clase 'title'
    titulo = driver.find_element(By.XPATH, "//h2[@class='title' and text()='Tabs']")
    titulo.click()

    # 2. Dar 2 TABs, escribir 'hola' y presionar ENTER para buscar
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys("hola").send_keys(Keys.ENTER).perform()

    time.sleep(2)