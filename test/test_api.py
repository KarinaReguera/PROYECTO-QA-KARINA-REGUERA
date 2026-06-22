import requests

import pytest_check as check  #Importo a la libreria pytest_check y la renombro como check
# Con pytest_check, ahora como check, ya no se usan los assert, se utiliza check."función" 
# Check hace que si el test falla en algun punto, siga evaluando el resto también
    # Para usar la librerúa pytest_check hay que instalarla: py -m install pytest_check

import pytest


#free_user_3EXtK4ArSiWNB7bOQKQ086N12rb

headers = {
    "x-api-key": "free_user_3EXtK4ArSiWNB7bOQKQ086N12rb"
}


#Los marcadores se ponen arriba de cada una de las pruebaS y se definen en archivo pytest.ini
#Para ejecutar ls pruebas por los marcadores se escribe en consola:
    #py -m pytest -m smoke           Ejecuta los test con marcador "smoke" de todos los archivos de test.
    #Si quiero ejecutar más de una etiqueta (marcador) se escribe en consola como un string:
        #py -m pytest -m "smoke or api"     Ejecuta las pruebas que son smoke o api
        #py -m pytest -m "smoke and api"    Ejecuta las pruebas que son smoke y también api
        #py -m pytest -m "not api"    Ejecuta todas las pruebas menos las api
@pytest.mark.api  # MARCADOR. llamo al marcador api dentro de la libreria de pytest
@pytest.mark.smoke  # Si quiero agregar más etiquetas, va debajo de la otra
def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    assert response.status_code == 200



@pytest.mark.api
def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
        "password": ""  #puedo sacar esta linea o dejarla con un string vacio, el resultado va a ser el mismo porque la API va a devolver un error 400 en ambos casos, ya sea porque falta el campo "password" o porque el campo "password" está vacío.
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json() # convierto la respuesta de la API a formato JSON y la guardo en la variable "body". Esto me permite acceder a los datos específicos de la respuesta, como el mensaje de error devuelto por la API.

    assert response.status_code == 400 #No puede crear el recurso por falta de contraseña
    #la prueba la va a pasar OK proque le indico que el status code esperado es 400, que es el que devuelve la API cuando falta el password. Si le indicara 200, la prueba fallaría porque no se cumple esa condición.

    assert body["error"] == "Missing password" # Verifico que el mensaje de error devuelto por la API sea "Missing password". Esto asegura que la API está devolviendo el mensaje de error correcto cuando falta el campo "password" en la solicitud de inicio de sesión. Si el mensaje de error no coincide, la prueba fallará, indicando que la API no está manejando correctamente la falta del campo "password".





@pytest.mark.api
def test_login_sin_email():
    body = {
        "email": "",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json() 
    
    assert response.status_code == 400
    assert body["error"] == "Missing email or username" 
    



@pytest.mark.api
def test_user_create_user():
    body = {
        "name": "John Doe",
        "email": "johndoe@reqres.in",
        "password": "1234567*"
        }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data = response.json() # convierto la respuesta de la API a formato JSON y la guardo en la variable "data". Esto me permite acceder a los datos específicos de la respuesta, como el ID del usuario creado, el nombre, etc. Es la respuesta del nuevo usuario creado.



    assert response.status_code == 201 # 201 Created: El recurso se ha creado exitosamente. En este caso, se espera que la API devuelva este código de estado cuando se crea un nuevo usuario correctamente.
    # Para evaluar códigos de estados, lo correcto es usar assert, si falla, no hace falta evaluar el resto. El ASSERT tiene mayor jerarquía que el CHECK.

    #check.equal(response.status_code,201) # digo response.status_code == 201. equial es una función de check. Es lo mismo que hacer la aserción de arriba
    


    #assert body["email"].count("@") == 1, "El formato del email es incorrecto"   
        # Verifico que el email enviado en el cuerpo de la solicitud contenga símbolo "@". Esto asegura que el formato es correcto. Si no contiene el símbolo "@" o si contiene más de uno, la prueba fallará, indicando que el formato del correo electrónico es incorrecto.

    check.equal(body["email"].count("@"),1) # Evaluo que en el email que se envía en el cuerpo de la solicitud contenga un "@"



    #assert "*" in body["password"]  
        # Verifico que la contraseña enviada en el cuerpo de la solicitud contenga al menos un carácter especial (en este caso, el símbolo "*"). Esto asegura que la contraseña cumple con ciertos requisitos de seguridad. Si la contraseña no contiene el carácter especial, la prueba fallará, indicando que la contraseña no cumple con los requisitos de seguridad.

    check.is_in("*",body["password"]) # Evaluo que "*" este en la contraseña. Uso la función de check.is_in



    #assert data["name"] == body["name"] 
        # Verifico que el nombre del usuario creado en la respuesta de la API sea igual al nombre que se envió en el cuerpo de la solicitud. Esto asegura que el usuario se creó con el nombre correcto.
    
    check.equal(data["name"],body["name"])



    #assert data["email"] == body["email"] 
        # Verifico que el correo electrónico del usuario creado en la respuesta de la API sea igual al correo electrónico que se envió en el cuerpo de la solicitud. Esto asegura que el usuario se creó con el correo electrónico correcto.

    check.equal(data["email"],body["email"])


    # body es lo que se envía en la solicitud para crear el usuario
    # data es lo que se guarda en el servidor después de crear el usuario



    #assert response.elapsed.total_seconds() < 1 
        # Verifico que el tiempo de respuesta de la API sea menor a los segundos indicados. Esto asegura que la API responde de manera rápida y eficiente. Si el tiempo de respuesta es mayor, la prueba fallará, indicando que la API no está respondiendo dentro del tiempo esperado.

    check.less(response.elapsed.total_seconds(),1) #Evaluo que response.elapsed.total_seconds() < 1 (el tiempo de respuesta < 1)


    print(response.elapsed.total_seconds())






@pytest.mark.api
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204 # 204 No Content: La solicitud se ha procesado correctamente, pero no hay contenido para devolver. En este caso, se espera que la API devuelva este código de estado cuando se elimina un usuario exitosamente.





@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/3", headers=headers)

    assert response.status_code == 200


    print(response.elapsed.total_seconds())

    assert response.elapsed.total_seconds() < 3, "El tiempo de ejecución tardó más de lo esperado"
    # Verifico que el tiempo de respuesta de la API sea menor a los segundos indicados. Esto asegura que la API responde de manera rápida y eficiente. Si el tiempo de respuesta es mayor, la prueba fallará, indicando que la API no está respondiendo dentro del tiempo esperado, muestra mensaje "El tiempo de ejecución tardó más de lo esperado".



