from selenium.webdriver.common.by import By # Importo la clase By para poder utilizar los selectores de elementos en Selenium.

from utils.logger import logger # Importo el logger para poder registrar eventos y mensajes durante la ejecución de los métodos de la clase LoginPage. 



# Esta clase representa la página de inicio de sesión (LoginPage) de una aplicación web. Contiene métodos para interactuar con los elementos de la página, como ingresar el nombre de usuario, la contraseña y hacer clic en el botón de inicio de sesión. También tiene un método para obtener el mensaje de error en caso de que el inicio de sesión falle.
class LoginPage:
    def __init__(self,driver): # El método __init__ es el constructor de la clase LoginPage. Recibe un parámetro driver, que es una instancia del controlador de Selenium (por ejemplo, ChromeDriver). Este controlador se utiliza para interactuar con el navegador web.
        self.driver =  driver  # Asigna el controlador de Selenium a un atributo de la clase para que pueda ser utilizado en otros métodos.


        # Selectores. Se capturan y guardan los selectores de los elementos de la página utilizando la clase By de Selenium. Estos selectores se utilizan para localizar los elementos en la página web y realizar acciones sobre ellos.
        self.username_input = (By.ID,"user-name") # Define un selector para el campo de entrada del nombre de usuario utilizando el método By.ID, que busca un elemento por su atributo ID. En este caso, el ID del campo de entrada es "user-name".
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_password = (By.CSS_SELECTOR, "[data-test='error']") # Define un selector para el mensaje de error utilizando el método By.CSS_SELECTOR, que busca un elemento utilizando un selector CSS. En este caso, se busca un elemento con el atributo data-test igual a "error", lo que indica que es el mensaje de error que se muestra cuando el inicio de sesión falla.
    

    def open(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
        except Exception as e:
            logger.critical("No se pudo conectar a la página") # Si ocurre una excepción al intentar abrir la página, se registra un mensaje de error crítico utilizando el logger para indicar que no se pudo conectar a la página. 

    

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)  # Utiliza el método find_element del controlador de Selenium para localizar el campo de entrada del nombre de usuario utilizando el selector definido anteriormente (self.username_input) y luego utiliza el método send_keys para ingresar el valor del nombre de usuario proporcionado como argumento (usuario).
            # Es decir, cuando quiero interactuar con un elemento de la página, utilizo el método find_element con el nombre de la variable que cree, en este cado "self.username_input".

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self,usuario,password):
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.error_password).text  
    
