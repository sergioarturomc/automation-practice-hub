import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Se ejecuta ANTES de cada test:
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver  # Le entrega el driver al test

    # Se ejecuta AL TERMINAR cada test:
    driver.quit()