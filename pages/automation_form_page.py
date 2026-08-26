import random
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class AutomationFormPage:
    ## selectores  necesarios

    field_name = (By.ID, 'name')
    field_email = (By.ID, 'email')
    field_phone = (By.ID, 'phone')
    field_address = (By.ID, 'textarea')
    field_gender_male = (By.ID, 'male')
    field_gender_female = (By.ID, 'female')
    field_days = (By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
    field_country = (By.ID, 'country')
    field_colors = (By.ID, 'colors')
    field_sorted_list = (By.ID, 'animals')
    field_datepicker1 = (By.ID, 'datepicker')
    field_datepicker2 = (By.ID, 'txtDate')
    select_month = (By.CLASS_NAME, 'ui-datepicker-month')
    select_year = (By.CLASS_NAME, 'ui-datepicker-year')
    field_start_date = (By.ID, 'start-date')
    field_custom_date = (By.XPATH, "//input[@type='date' or contains(@class, 'picker')]")
    btn_month_year_header = (By.XPATH, "//button[contains(@class, 'month-year') or contains(text(), '202')]")
    field_end_date = (By.ID, 'end-date')
    btn_submit_range = (By.CLASS_NAME, 'submit-btn')

    ##inicio de funciones

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    ##FUNCIONES EXTRAS

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    ## FUNCIONES BASICAS

    def set_name(self, name_form):
        self._find(self.field_name).send_keys(name_form)

    def set_email(self, email_form):
        self._find(self.field_email).send_keys(email_form)

    def set_phone(self, phone_form):
        self._find(self.field_phone).send_keys(phone_form)

    def set_address(self, address_form):
        self._find(self.field_address).send_keys(address_form)

    def set_gender(self, gender_form):
        self._click(self.field_gender_male)

    def set_days(self, days_form):
        checkboxes = self._find_all(self.field_days)
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()

    def set_country(self, field_country):
        select_element = self._find(self.field_country)
        dropdown = Select(select_element)
        dropdown.select_by_visible_text('Japan')

    def set_colors(self, ):
        select_element = self._find(self.field_colors)
        dropdown = Select(select_element)
        options = dropdown.options
        random_option = random.choice(options)
        dropdown.select_by_visible_text(random_option.text)

    def set_sorted_list(self):
        select_element = self._find(self.field_sorted_list)
        dropdown = Select(select_element)
        options = dropdown.options
        random_option = random.choice(options)
        dropdown.select_by_visible_text(random_option.text)

    def set_datepicker1(self, field_datepicker1):
        field = self._find(self.field_datepicker1)
        field.clear()
        field.send_keys(field_datepicker1)

    def set_datepicker2(self, month_name, year_val, day_num):

        # 1. Clic en la casilla para desplegar el calendario
        self._click(self.field_datepicker2)

        # 2. Seleccionar el Mes (ej: "Jan", "Oct", "Dec")
        month_dropdown = Select(self._find(self.select_month))
        month_dropdown.select_by_visible_text(month_name)

        # 3. Seleccionar el Año (ej: "2017" o "2020")
        year_dropdown = Select(self._find(self.select_year))
        year_dropdown.select_by_visible_text(str(year_val))

        # 4. Clic en el número de Día
        day_locator = (By.XPATH, f"//table[@class='ui-datepicker-calendar']//a[text()='{day_num}']")
        self._click(day_locator)

    def set_datepicker3(self, start_date="08192026", end_date="08252026"):
        # Se envía directamente la ráfaga de números sin guiones
        self._find(self.field_start_date).send_keys(start_date)
        self._find(self.field_end_date).send_keys(end_date)

        # Clic en el botón Submit
        self._click(self.btn_submit_range)

    ##### UPLOAD FILES ###

    ##Selectores necesarios

    input_single_file = (By.ID, 'singleFileInput')
    input_multi_file = (By.ID, 'multipleFilesInput')
    btn_upload_single = (By.XPATH, "//button[text()='Upload Single File']")
    btn_upload_multiple = (By.XPATH, "//button[text()='Upload Multiple Files']")


    def upload_single_file(self, file_name):
        file_path = os.path.abspath(os.path.join("imagenes", file_name))
        self._find(self.input_single_file).send_keys(file_path)
        self._click(self.btn_upload_single)

    def upload_multiple_files(self, file_names):
        ## en esta parte utilize  ayuda de la AI por que no sabia como representar el tema de el path para subir archivos
        file_paths = "\n".join([os.path.abspath(os.path.join("imagenes", f)) for f in file_names])
        self._find(self.input_multi_file).send_keys(file_paths)
        self._click(self.btn_upload_multiple)




