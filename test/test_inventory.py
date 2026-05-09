# Este archivo contiene varias pruebas que verifica una cosa cada una.
# como que el título de la página del inventario sea correcto, que se muestren los productos, que estén visibles los elementos de la UI (menu hamburguesa y filtro).
# Cada prueba es independiente.





from selenium import webdriver # Importo el módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  # Importo el módulo By para localizar elementos en la página web.
import pytest  # Importo el módulo pytest para usar los fixtures y las aserciones en los test.



@pytest.fixture
def driver_logged (login_in_driver): # El fixture driver_logged, depende del fixture login_in_driver, que hace el login y devuelve el driver con el login ya hecho, para que el test pueda usarlo sin tener que repetir el código de login en cada test.
    
    drive = login_in_driver  # El fixture login_in_driver, hace el login y devuelve el driver con el login ya hecho, para que el test pueda usarlo sin tener que repetir el código de login en cada test.
    
    return drive  # Devuelvo el driver con el login ya hecho, para que los test puedan usarlo sin tener que repetir el código de login en cada test.



def test_inventario_title(driver_logged):
    
    titulo = driver_logged.title    # Se obtiene el valor del title de la pagina.
    
    assert titulo == "Swag Labs", f"El título de la página es incorrecto, se esperaba 'Swag Labs'" 
            #Se compara el valor del title con el valor esperado, si no coincide, se muestra un mensaje de error con el valor obtenido.  



def test_productos(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")  
            # Se buscan los elementos con la clase "inventory_item", que son los productos, y se guardan en una lista.
    assert len(productos) > 0, f"Se esperaba encontrar productos visibles"
            # Se verifica que la lista de productos no esté vacía. Si está vacía, se muestra un mensaje de error indicando que se esperaba encontrar productos visibles



def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")  # Se busca el elemento del menú por su ID.

    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")  # Se busca el elemento del filtro por su clase.


    assert menu.is_displayed(), "El ícono del menú no se muestra en la página del inventario" 
            # Se verifica que el botón del menú esté visible, si no está visible, se muestra un mensaje de error indicando que el botón del menú no se muestra en la página de inventario.

    assert filtro.is_displayed(), "El filtro de productos no se muestra en la página del inventario"
            # Se verifica que el filtro de productos esté visible, si no está visible, se muestra un mensaje de error indicando que el filtro de productos no se muestra en la página de inventario.







