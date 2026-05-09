# conftest.py   
# Este archivo conftest.py, es un archivo de configuración para los test, donde se definen los fixtures que se van a usar en los test.

# las funciones definidas como fixture, son funciones globales, que pueden ser utilizadas por cualquier test, sin necesidad de importarlas, solo con poner el nombre del fixture como argumento en la función del test, se ejecuta el fixture antes de ejecutar el test.




import pytest  # Importo el módulo pytest para usar los fixtures y las aserciones en los test.

from selenium import webdriver # Importo el módulo webdriver de Selenium para controlar el navegador.

from utils.LoginPage import login  # Importo la función login del archivo LoginPage que está en la carpeta utils, para usarla en el fixture login_in_driver, que hace el login antes de cada test. 





# Este fixture configura el driver, que se va a usar en los test, y se cierra al finalizar cada test.
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()  # Creo una instancia de ChromeOptions para configurar el navegador Chrome.
    options.add_argument("--incognito")  # Agrego el argumento "--incognito" para abrir el navegador en modo incógnito, lo que evita que se guarden cookies, historial y otros datos de navegación. 
    driver = webdriver.Chrome(options=options)  # Creo una instancia del navegador Chrome utilizando las opciones configuradas y lo asigno a la variable "driver".

    yield driver    # Se ejecutan las instrucciones de la función "def login(driver)" que se importo de utils/LoginPage.py
    
    driver.quit()  # dirver.quit() cierra el navegador después de cada test para liberar recursos y evitar que queden procesos abiertos.




# Este fixture hace el login antes de cada test, utilizando el driver configurado en el fixture anterior, y devuelve el driver con el login ya hecho, para que los test puedan usarlo sin tener que repetir el código de login en cada test.

@pytest.fixture
def login_in_driver(driver):    # Inicia sesión con toda la configuración del driver.
    
    login(driver)   # llamo a la función login que importe al inicio y le paso el driver como argumento.
    
    return driver   # Devuelvo el driver con el login ya hecho, para que los test puedan usarlo sin tener que repetir el código de login en cada test.

