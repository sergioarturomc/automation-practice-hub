from selenium.webdriver.common.by import By
import data


def test_static_webtable_page_validactions(driver):
    driver.get(data.url)

    # 1. Contar filas de datos especificando name='BookTable'
    rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[position()>1]")
    assert len(rows) == 6

    # 2. Sumar la columna Price solo de esta tabla
    prices = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[position()>1]/td[4]")
    total_price = sum(int(p.text) for p in prices)
    assert total_price == 7100

    # 3. Buscar precio de 'Master In Selenium' en esta tabla
    price_element = driver.find_element(
        By.XPATH, "//table[@name='BookTable']//tr[td[1]='Master In Selenium']/td[4]"
    )
    assert price_element.text == "3000"


    ## 4 Seria lo mismo para buscar cualquier otro libro y su precio
