from page.login_page import LoginPage  # Importo la clase LoginPage desde el módulo page.login_page para poder utilizarla en los tests de inicio de sesión.

# IMPORTO EL LECTOR
from utils.data_reader import read_user_csv # Importo la función read_user_csv desde el módulo utils.data_reader para poder leer los datos de los usuarios desde un archivo CSV y utilizarlos en los tests de inicio de sesión.


import pytest


# PARAMETRIZO el LECTOR con la PRUEBA.
# parametrizo el test de inicio de sesión utilizando los datos de los usuarios obtenidos del archivo CSV. Cada diccionario de usuario se asignará al parámetro "user" en el test, lo que permite ejecutar cada test con diferentes conjuntos de datos de usuarios.
                        # se captura al usuario que viene de la función read_user_csv() 
@pytest.mark.parametrize("user", read_user_csv()) 
# @pytest.mark.parametrize: Le dice a Pytest que ejecute la función múltiples veces con diferentes datos.

def test_login_csv(driver, user): 
    login_page = LoginPage(driver) # Creo una instancia de la clase LoginPage, pasando el driver como argumento para poder interactuar con la página de inicio de sesión durante el test.

    # Inicio sesión
    login_page.login(user["username"], user["password"]) # Llamo a la función "login" que está dentro del archivo "login_page.py", llamando al método login de la instancia login_page, pasando el nombre de usuario y la contraseña obtenidos del diccionario "user" para realizar el intento de inicio de sesión durante el test.

    # Valido si el usuario es incorrecto
    if user["valid"] == "true": # Si el valor del campo "valid" en el diccionario "user" es igual a "true", entonces se espera un inicio de sesión exitoso.
        # Validación de la página correcta, luego de iniciar sesión
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"


    else:
        error = login_page.get_error_message()
        assert "Epic sadface" in error  # Verifico que el mensaje de error obtenido del método get_error_message de la clase LoginPage contenga la cadena "Epic sadface", lo que indica que se ha producido un error de inicio de sesión debido a credenciales incorrectas.



