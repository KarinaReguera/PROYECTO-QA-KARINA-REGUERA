# conftest.py   
# Este archivo conftest.py, es un archivo de configuración para los test, donde se definen los fixtures que se van a usar en los test.

# las funciones definidas como fixture, son funciones globales, que pueden ser utilizadas por cualquier test, sin necesidad de importarlas, solo con poner el nombre del fixture como argumento en la función del test, se ejecuta el fixture antes de ejecutar el test.


import pytest  # Importo el módulo pytest para poder utilizar los decoradores y funciones de pytest en la definición de los fixtures. 

from selenium import webdriver  # Importo el módulo webdriver de Selenium para poder utilizarlo en la creación del controlador del navegador.

from page.login_page import LoginPage # Importo la clase LoginPage desde el módulo page.login_page para poder utilizarla en el fixture driver_logged, que se encarga de iniciar sesión antes de ejecutar los tests que requieren un usuario logueado.

from utils.data_reader import read_user_csv # Importo la función read_user_csv desde el módulo utils.data_reader para poder leer los datos de los usuarios desde un archivo CSV y utilizarlos en el fixture driver_logged para iniciar sesión con un usuario específico antes de ejecutar los tests que requieren un usuario logueado.

import pathlib # Importo el módulo pathlib para poder utilizarlo en la función read_user_csv para construir la ruta del archivo CSV de manera más flexible y compatible con diferentes sistemas operativos.

import pytest_html # Importo el módulo pytest_html para poder utilizarlo en la función pytest_runtest_makereport para agregar la captura de pantalla al informe HTML generado por pytest.






# El fixture driver, es un fixture que se encarga de crear una instancia del navegador Chrome, con las opciones de incognito, y luego de ejecutar el test, cierra el navegador. Este fixture se utiliza en los tests para poder interactuar con el navegador y realizar las pruebas de automatización.
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options = options)

    yield driver

    driver.quit()




# CONFIGURACION GLOBAL PARA INICIAR SESION CON USUARIO VALIDO ANTES DE EJECUTAR LOS TESTS QUE REQUIEREN UN USUARIO LOGUEADO.
@pytest.fixture
def driver_logged(driver):
    # El fixture driver_logged, es un fixture que se encarga de iniciar sesión en la aplicación antes de ejecutar el test, utilizando el fixture driver para interactuar con el navegador. Este fixture se utiliza en los tests que requieren que el usuario esté logueado para poder realizar las pruebas de automatización.
        
    # Inicio el navedador
    login_page = LoginPage(driver) # Creo una instancia de la clase LoginPage, pasando el driver como argumento para poder interactuar con la página de inicio de sesión durante el proceso de inicio de sesión en el fixture.

    user = read_user_csv()[0] # Llamo a la función read_user_csv para obtener la lista de usuarios desde el archivo CSV, y luego selecciono el primer usuario de la lista (índice 0) para utilizarlo en el proceso de inicio de sesión en el fixture driver_logged. Es el usuario VALIDO.

    # Inicio sesión con datos válidos
    login_page.login(user["username"], user["password"]) # Llamo a la función login que está dentro del archivo login_page.py, llamando al método login de la instancia login_page, pasando el nombre de usuario y la contraseña obtenidos del diccionario user para realizar el inicio de sesión antes de ejecutar los tests que requieren un usuario logueado.

    # Retorno "driver" que es el navegador logueado
    return driver





#    CAPTURA DE PANTALLA CUANDO FALLA UN TEST
@pytest.hookimpl(tryfirst=True, hookwrapper=True) # Decorador de pytest que indica que la función pytest_configure se ejecutará antes de cualquier otro hook de configuración y que es un wrapper, lo que significa que puede ejecutar código antes y después de la ejecución del hook original.

def pytest_runtest_makereport(item, call): #Se ejecuta después de cada fase (setup/call/teardown) de cada test. La función recibe dos argumentos: item, que representa el test actual, y call, que representa la llamada al test. 

    outcome = yield  # Yield para permitir que el test se ejecute y luego continuar con la ejecución del código después del test. Permite que Pytest genere el reporte.

    report = outcome.get_result()  # Obtiene el resultado de la ejecución del test después de que se haya completado. Se obtiene el objeto report. El objeto report contiene información sobre el resultado del test, como si ha pasado o ha fallado, y en qué fase del test ocurrió el resultado.

    # when puede ser "setup", "call" o "teardown", dependiendo de la fase del test que se esté ejecutando. 
    if report.when == "call" and report.failed:  # verifica si el resultado del test es un fallo (report.failed) y si la fase del test es "call" (report.when == "call"). Esto significa que el test ha fallado durante la fase de ejecución, lo que indica que el código del test ha producido un error o una excepción. Si ambas condiciones se cumplen, se procede a tomar una captura de pantalla del estado actual del navegador para ayudar a diagnosticar el problema que causó el fallo del test.

        driver = item.funcargs.get("driver")  # se obtiene el driver del test actual utilizando el diccionario funcargs, que contiene los argumentos de la función del test. Si el test utiliza el fixture "driver", se obtiene el driver para poder tomar una captura de pantalla en caso de que el test falle. Esto es importante para evitar errores adicionales en caso de que el test no utilice el fixture "driver" o si el driver no se ha inicializado correctamente.
        
        if driver:  # Verifica si se ha obtenido un driver válido antes de intentar tomar una captura de pantalla. Esto es importante para evitar errores adicionales en caso de que el test no utilice el fixture "driver" o si el driver no se ha inicializado correctamente.

            target= pathlib.Path("reports/screenshots") # Construye la ruta del directorio donde se guardarán las capturas de pantalla utilizando pathlib.Path para una construcción de rutas más flexible y compatible con diferentes sistemas operativos.

            target.mkdir(parents=True, exist_ok=True) # Crea el directorio de destino si no existe, utilizando el método mkdir de pathlib.Path con los argumentos parents=True para crear cualquier directorio padre necesario y exist_ok=True para evitar errores si el directorio ya existe.

            file_name = target / f"{item.name}.png" # Construye la ruta completa del archivo de captura de pantalla utilizando el nombre del test (item.name) para nombrar el archivo PNG.

            driver.save_screenshot(str(file_name)) # Toma una captura de pantalla del estado actual del navegador utilizando el método save_screenshot del driver, y guarda la imagen en la ruta especificada por file_name. La función str() se utiliza para convertir el objeto Path a una cadena de texto que representa la ruta del archivo, ya que el método save_screenshot espera una cadena como argumento. Esto permite guardar una captura de pantalla con el nombre del test que ha fallado, lo que facilita la identificación de los problemas durante la ejecución de los tests.


            #ADJUNTO AL REPORTE HTML LA CAPTURA DE PANTALLA CUANDO FALLA UN TEST
            if hasattr(report, "extra"):  # la función "hasattr() verifica si el informe del test tiene un atributo "extra" para agregar información adicional al informe de pytest. En este caso una columna extra para agregar la captura de pantalla del error.

                report.extra.append(
                    {
                    "name": "screenshot",  # Nombre que se mostrará en el informe HTML para la columna de la captura de pantalla.
                    "format": "image",  # Formato de la información que se agregará a la columna de la captura de pantalla, indicando que se trata de una imagen.
                    "content": str(file_name)  # Contenido que se agregará a la columna de la captura de pantalla, que es la ruta del archivo de la captura de pantalla convertida a una cadena de texto para que se muestre correctamente en el informe HTML.
                    }
                )

            extras = getattr(report, "extra", [])  # Obtiene el atributo "extra" del informe del test, o una lista vacía si el atributo no existe, para asegurarse de que se pueda agregar la información adicional de la captura de pantalla al informe de pytest sin causar errores. Esto es útil para agregar la captura de pantalla al informe HTML generado por pytest, lo que facilita la identificación de los problemas durante la ejecución de los tests al mostrar la imagen del estado del navegador en el momento en que ocurrió el error.

            extras.append(pytest_html.extras.png(str(file_name)))  # Agrega la captura de pantalla al informe HTML utilizando pytest_html.extras.png para indicar que se trata de una imagen PNG, y pasando la ruta del archivo de la captura de pantalla convertida a una cadena de texto. Esto permite que la captura de pantalla se muestre correctamente en el informe HTML generado por pytest, lo que facilita la identificación de los problemas durante la ejecución de los tests al mostrar la imagen del estado del navegador en el momento en que ocurrió el error.

            report.extras = extras  # Asigna la lista de extras actualizada al informe del test para que la información adicional de la captura de pantalla se incluya en el informe HTML generado por pytest. Esto asegura que la captura de pantalla se muestre correctamente en el informe HTML, lo que facilita la identificación de los problemas durante la ejecución de los tests al mostrar la imagen del estado del navegador en el momento en que ocurrió el error.




