from selenium import webdriver # Importo el módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  # Importo el módulo By para localizar elementos en la página web.



def login(driver):
    # Abre página web
    driver.get("https://www.saucedemo.com/") # Abre la página web de SauceDemo utilizando el método get() del driver.

    # Ingreso el usuario
    usuario = driver.find_element(By.ID, "user-name") # Localizo el campo de usuario por su ID "user-name" y lo asigno a la variable "usuario".
    usuario.send_keys("standard_user") # Envío el texto "standard_user" al campo de usuario utilizando el método send_keys().

    # Ingreso la contraseña
    password = driver.find_element(By.ID, "password") # Localizo el campo de contraseña por su ID "password" y lo asigno a la variable "password".
    password.send_keys("secret_sauce") # Envío el texto "secret_sauce" al campo de contraseña utilizando el método send_keys().

    # Click en botón de Login
    boton_login = driver.find_element(By.ID, "login-button") # Localizo el botón de login por su ID "login-button" y lo asigno a la variable "boton_login".
    boton_login.click() # Hago clic en el botón de login utilizando el método click().


