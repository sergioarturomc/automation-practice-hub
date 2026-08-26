import time
# Importamos la clase que definiste en tu otro archivo
from pages.automation_form_page import AutomationFormPage
# Si está dentro de una carpeta llamada "pages":
import data
# Asumiendo que data.py contiene variables como url, name, etc.


### Test Form

def test_data_entry_form(driver):
    # 1. Navegar a la URL (usando la variable real de tu archivo data.py)
    driver.get(data.url)

    # 2. Usar el objeto
    form_page = AutomationFormPage(driver)

    # 3. Ejecutar los métodos y usar el objeto
    form_page.set_name(data.name_form)
    form_page.set_email(data.email_form)
    form_page.set_phone(data.phone_form)
    form_page.set_address(data.adress_form)

    ### en este objeto tenemos 2 roles male y female en el data es mas sencillo cambiarlo si
    ### necesito hacer una prueba diferenete

    form_page.set_gender(data.gender_form)

    ## Aqui podemos elejir 1 solo dia o los 7 dias dando clic
    ## seleccionamos todos los dias usando un selector xptah
    ## o podemos usar lo datos en data.py para seleccionar 1 solo dia

    form_page.set_days(data.days_form)

    form_page.set_country("Japan")

    ## Seleccionamos un color al azar la pagina es gratis para pruebas QA de Automatizacion
    ## por lo cual existe un error donde seleccionas un color y se deseleciona cuando pasas al siguiente
    ## campo
    form_page.set_colors()

    ## en este ejemplo tambien sucedio lo mismo se deselecciona al avanzar al siguiente paso BUG
    form_page.set_sorted_list()

    form_page.set_datepicker1("08/25/2026")

    # Ejemplo para seleccionar Octubre 01, 2017 o cualquier otra fecha solo cambiando los valores string"oct" etc
    ## utilize Ayuda de la AI por que no encontraba la forma mas sencilla de poder cambiar las fechas a mi favor para algun test
    form_page.set_datepicker2(month_name="Oct", year_val="2017", day_num="1")

    # Selecciona un rango de fecha

    form_page.set_datepicker3()

    ###### aqui termina la primera parte de practia ####









    time.sleep(5)