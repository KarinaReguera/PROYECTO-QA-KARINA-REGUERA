# Este archivo test_login-py, solo se va a utilizar para hacer pruebas del login


from selenium import webdriver  # Importo el módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  # Importo el módulo Keys para simular teclas del teclado, como Enter, Tab, etc.




# Defino las pruebas

def test_login_exitoso(login_in_driver):   # Paso el fixture "login_in_driver" que está definido en el archivo "conftest.py".

    driver = login_in_driver  # Guardo en una variable "driver" el "login_in_driver" que es el fixture que hace el login y devuelve el driver con el login OK y redirigido a la página del inventario.
        
    # Verificar URL        
    assert "/inventory.html" in driver.current_url, "Login fallido, no se redirigió a la página de inventario"
            # Se verifica que la URL actual del navegador contenga "/inventory.html", lo que indica que el login fue exitoso y se redirigió a la página de inventario. Si no se cumple esta condición, se muestra un mensaje de error indicando que el login falló y no se redirigió a la página de inventario.



