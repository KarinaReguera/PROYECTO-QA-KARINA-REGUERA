from selenium import webdriver # Importo el módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  # Importo el módulo By para localizar elementos en la página web.
import pytest  # Importo el módulo pytest para usar los fixtures y las aserciones en los test.

from page.inventory_page import InventoryPage # Importo la clase InventoryPage desde el módulo page.inventory_page para poder utilizarla en los tests relacionados con el inventario.

from page.login_page import LoginPage  # Importo la clase LoginPage desde el módulo page.login_page para poder utilizarla en los tests de inicio de sesión.




def test_inventario_title(driver_logged): # Se pasa la función globalizada creada en conftest.py, que se encarga de iniciar sesión antes de ejecutar el test, utilizando el fixture driver para interactuar con el navegador. Este fixture se utiliza en los tests que requieren que el usuario esté logueado para poder realizar las pruebas de automatización.

    # En cada test se crea el OBJETO CONSTRUCTOR de las funciones relacionada con la página del inventario.
    inventory_page = InventoryPage(driver_logged)   # Creo una instancia de la clase InventoryPage, pasando el driver_logged como argumento para poder interactuar con la página del inventario durante las pruebas.

    titulo = inventory_page.obtener_titulo()

    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"
    # Utilizo una aserción para verificar que el título obtenido (titulo) es igual a "Swag Labs". Esto indica que el título de la página de inventario es correcto. Si la aserción falla, se mostrará el mensaje "El título del inventario no es correcto" para indicar que el título no coincide con lo esperado.




#Los marcadores se ponen arriba de cada prueba y se definen en archivo pytest.ini
@pytest.mark.smoke  # MARCADOR. llamo al marcador "smoke" dentro de la libreria de pytest
def test_productos_visibles(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    productos = inventory_page.obtener_productos()
    assert len(productos) > 0
    # Utilizo una aserción para verificar que la cantidad de productos obtenidos (productos) es mayor a 0. Esto indica que hay productos visibles en la página de inventario. Si la aserción falla, se mostrará el mensaje "No hay productos visibles en el inventario" para indicar que no se encontraron productos en la página.




def test_ui_elements(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    assert inventory_page.menu_visible(), "El menu no está presente en la pagina"

    assert inventory_page.filtro_visible(), "El filtro no está presente en la pagina"
    # Utilizo aserciones para verificar que el menú y el filtro están visibles en la página de inventario. Si alguna de las aserciones falla, se mostrará un mensaje indicando que el elemento correspondiente no está presente en la página.







