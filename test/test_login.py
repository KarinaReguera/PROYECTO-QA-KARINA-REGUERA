# Este archivo contiene los tests relacionados con el inicio de sesión en la aplicación web. Se importan las clases y funciones necesarias para realizar las pruebas, como LoginPage para interactuar con la página de inicio de sesión y logger para registrar eventos durante la ejecución de los tests.


from page.login_page import LoginPage
# Importo la clase LoginPage desde el módulo page.login_page para poder utilizarla en los tests de inicio de sesión.

from utils.logger import logger

import pytest




#Los marcadores se ponen arriba de cada prueba y se definen en archivo pytest.ini
@pytest.mark.smoke  # MARCADOR. llamo al marcador "smoke" dentro de la libreria de pytest
def test_login_ok(driver):
    login_page = LoginPage(driver) # Creo una instancia de la clase LoginPage, pasando el controlador de Selenium (driver) como argumento. Esto me permite utilizar los métodos definidos en la clase LoginPage para interactuar con la página de inicio de sesión.
    
    logger.info("Inicializando el driver para el test-login_ok") # Utilizo el logger para registrar un mensaje de información indicando que se está inicializando el driver para el test de inicio de sesión exitoso (test-login_ok). Esto me permite tener un registro de los eventos que ocurren durante la ejecución del test, lo que facilita la depuración y el seguimiento de los resultados del test.

    login_page.login("standard_user","secret_sauce") # Llamo al método login de la clase LoginPage, pasando el nombre de usuario "standard_user" y la contraseña "secret_sauce" como argumentos. Esto simula el proceso de inicio de sesión en la aplicación web.
    
    logger.info("Ingresando los datos de entrada para la prueba")
    
    logger.info("Iniciando sesión...")

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario" # Utilizo una aserción para verificar que la URL actual del navegador (driver.current_url) contiene la cadena "/inventory.html". Esto indica que el inicio de sesión fue exitoso y que se redirigió a la página de inventario. Si la aserción falla, se mostrará el mensaje "No se redirigió al inventario" para indicar que el inicio de sesión no fue exitoso.

    if "/inventory.html" in driver.current_url: # Verifico nuevamente si la URL actual del navegador contiene la cadena "/inventory.html". Esto me permite registrar un mensaje de información adicional utilizando el logger para indicar que el inicio de sesión fue exitoso y que se redirigió a la página de inventario.
        logger.info("Sesión iniciada correctamente")
    else:
        logger.error("No se pudo iniciar sesión. No se redirigió al inventario") # Si la URL no contiene la cadena "/inventory.html", registro un mensaje de error utilizando el logger para indicar que no se pudo iniciar sesión correctamente.
        




def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    logger.info("Inicializando el driver para el test-login_invalid_password") # Utilizo el logger para registrar un mensaje de información indicando que se está inicializando el driver para el test de inicio de sesión con contraseña inválida (test-login_invalid_password). Esto me permite tener un registro de los eventos que ocurren durante la ejecución del test, lo que facilita la depuración y el seguimiento de los resultados del test.

    login_page.login("standard_user","123456")

    logger.info("Ingresando los datos de entrada para la prueba")
    
    logger.info("No se pudo iniciar sesión debido a una contraseña incorrecta")
    
    error = login_page.get_error_message() # Llamo al método get_error_message de la clase LoginPage para obtener el mensaje de error que se muestra en la página cuando el inicio de sesión falla debido a una contraseña incorrecta. El mensaje de error se almacena en la variable error.

    assert "Epic sadface: Username and password do not match any user in this service" in error  # Utilizo una aserción para verificar que el mensaje de error obtenido (error) contiene la cadena "Epic sadface: Username and password do not match any user in this service". Esto indica que el mensaje de error es el esperado cuando se ingresa una contraseña incorrecta. Si la aserción falla, se mostrará un mensaje de error indicando que el mensaje de error no es el esperado.

    #assert error == "Falla" # fuerzo el error para que falle y se muestre la captura de pantalla, ya que el mensaje de error real no es "Hola". Esto me permite verificar que la funcionalidad de captura de pantalla en caso de fallo del test está funcionando correctamente. Si la aserción falla, se mostrará un mensaje de error indicando que el mensaje de error no es el esperado.


