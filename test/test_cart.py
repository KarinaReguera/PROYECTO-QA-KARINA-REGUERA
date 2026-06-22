# Esta es una sola prueba que verifica varias cosas. 
# como que se pueda agregar un producto al carrito, que el contador del carrito se actualice correctamente, que el producto agregado al carrito sea el mismo que se muestra en la página del carrito, etc.




from selenium import webdriver # Importo el módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  # Importo el módulo By para localizar elementos en la página web.
import pytest  # Importo el módulo pytest para usar los fixtures y las aserciones en los test.




#Los marcadores se ponen arriba de cada prueba y se definen en archivo pytest.ini
@pytest.mark.smoke  # MARCADOR. llamo al marcador "smoke" dentro de la libreria de pytest
def test_cart(driver_logged):   # Paso el fixture "login_in_driver" que está definido en el archivo "conftest.py".

    driver = driver_logged  # Asigno el valor del fixture "driver_logged" a la variable "driver" para poder utilizarlo en el test. El fixture "driver_logged" se encarga de iniciar sesión en la aplicación antes de ejecutar el test, utilizando el fixture "driver" para interactuar con el navegador. Este fixture se utiliza en los tests que requieren que el usuario esté logueado para poder realizar las pruebas de automatización. 


    # Agregar un producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click() 
                # Busca el primer botón de "Agregar al carrito" por su clase "btn_inventory" y hace clic en él para agregar el producto al carrito.
                # No es necesario guardarlo en una variable. Se puede hacer directamente "driver.find_element(By.class_NAME, "btn_inventory")[0].click()"

    # Verificar que el producto se agregó al contador del carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text 
                # Busca el elemento del carrito por su clase "shopping_cart_badge", que es el contador que muestra la cantidad de productos en el carrito, obtiene su texto (string) y lo guarda en la variable "contador_cart".

    assert contador_cart == "1", "La cantidad de productos del carrito no se agregó correctamente" 
                # Se verifica que el texto del contador del carrito sea "1", lo que indica que se agregó un producto al carrito. Si no se cumple esta condición, se muestra un mensaje de error indicando que el producto no se agregó al carrito.


    # Obtener el nombre del 1º producto agregado al carrito
    nombre_producto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text 
                # Busca el primer elemento con la clase "inventory_item_name", que es el nombre del producto, obtiene su texto (string) y lo guarda en la variable "nombre_producto".  



    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() 
                # Busca el elemento del carrito por su clase "shopping_cart_link" y hace clic en él para ir a la página del carrito.

    # Obtener el nombre del producto en el carrito
    producto_en_carrito = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text 



    # Verificar que el producto en el carrito sea el mismo que se agregó
    assert producto_en_carrito == nombre_producto, "El producto en el carrito no coincide con el producto agregado" 
                # Se verifica que el nombre del producto en el carrito sea igual al nombre del producto que se agregó, lo que indica que el producto correcto se agregó al carrito. Si no se cumple esta condición, se muestra un mensaje de error indicando que el producto en el carrito no coincide con el producto agregado.









