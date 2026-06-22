# Se definen los pasos a realizar en cada accion

from page.login_page import LoginPage # Importamos la clase LoginPage del archivo login_page.py para poder utilizar sus recursos 

from behave import given, when, then



#Para cada paso se crea una funcion que se ejecutara al realizar la accion definida en el archivo .feature

# GIVEN: es la precondicón, que el usuario este en la pagina del login.
@given("que el usuario este en la pagina del Login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver) # Se crea una instancia de la clase LoginPage y le pasamos el driver del navegador para poder interactuar con la pagina. INICIALIZO LA CLASE LoginPage Y LE PASO EL driver PARA PODER UTILIZAR SUS RECURSOS

    context.login_page.open() # Llama a la funcion open() de la clase LoginPage para abrir la pagina del login. Esa función tiene la URL de la pagina del login definida, por lo que al llamarla se abre esa pagina en el navegador.




# WHEN: es la accion que se realiza, en este caso el usuario ingresa su email y contraseña y hace click en el boton de login.
@when("ingresa el usuario '{usuario}' y contraseña '{password}'")
def step_ingresar_credenciales(context,usuario,password):
    if usuario == "VACIO":
        usuario = ""
    if password =="VACIO":
        password = ""

    context.login_page.ingresar_usuario(usuario) # Llama a la funcion ingresar_usuario() de la clase LoginPage para ingresar el nombre de usuario proporcionado como argumento (usuario) en el campo de entrada del nombre de usuario en la pagina del login.
    context.login_page.ingresar_password(password) # Llama a la funcion ingresar_password() de la clase LoginPage para ingresar la contraseña proporcionada como argumento (password) en el campo de entrada de la contraseña en la pagina del login.



@when("hace clic en el boton Login")
def step_click_login(context):
    context.login_page.click_login() # Llama a la funcion click_login() de la clase LoginPage para hacer clic en el botón de inicio de sesión en la pagina del login. Esto simula la acción de un usuario haciendo clic en el botón para intentar iniciar sesión.



@then("deberia ingresar a la pagina del inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url, "No se redirigió al inventario" # Uso el assert de la función "test_login_ok" que está en el archivo test_login.py, PERO agrego despues del in context., queda "context.driver.current_url" para verificar que la URL actual del navegador contiene la cadena "/inventory.html". Esto indica que el inicio de sesión fue exitoso y que se redirigió a la página de inventario. Si la aserción falla, se mostrará el mensaje "No se redirigió al inventario" para indicar que el inicio de sesión no fue exitoso.



@then("deberia dar el mensaje de error '{mensaje}'")
def step_validar_mensaje_error(context, mensaje):
    error = context.login_page.get_error_message() # Llama a la función get_error_message() de la clase LoginPage para obtener el mensaje de error que se muestra en la página cuando el inicio de sesión falla. El mensaje de error se almacena en la variable error. CAPTURA EL MENSAJE DE ERROR QUE SE MUESTRA EN LA PAGINA CUANDO EL INICIO DE SESION FALLA Y LO ALMACENA EN LA VARIABLE error.

    assert mensaje in error, f"El mensaje de error no es el esperado. Se esperaba: '{mensaje}', pero se obtuvo: '{error}'" # Utiliza una aserción para verificar que el mensaje de error obtenido (error) contiene la cadena proporcionada como argumento (mensaje). Esto indica que el mensaje de error es el esperado cuando el inicio de sesión falla. Si la aserción falla, se mostrará un mensaje de error indicando que el mensaje de error no es el esperado, junto con los valores esperados y obtenidos para facilitar la depuración.

