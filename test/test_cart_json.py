from selenium import webdriver # Importo el módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.common.by import By  # Importo el módulo By para localizar elementos en la página web.
import pytest  # Importo el módulo pytest para usar los fixtures y las aserciones en los test.


from page.inventory_page import InventoryPage  # Importo la clase InventoryPage desde el archivo inventory_page.py para usar sus métodos en el test.

from page.cart_page import CartPage  # Importo la clase CartPage desde el archivo cart_page.py para usar sus métodos en el test.

from utils.data_reader import read_product_json  # Importo la función read_product_json desde el



def test_cart_json(driver_logged):  # Defino una función de test llamada test_cart_json que recibe un fixture driver_logged para controlar el navegador.

    inventory_page = InventoryPage(driver_logged)  # Creo una instancia de InventoryPage pasando el driver_logged para interactuar con la página de inventario.

    cart_page = CartPage(driver_logged)  # Creo una instancia de CartPage pasando el driver_logged para interactuar con la página del carrito.

    productos = read_product_json()  # Llamo a la función read_product_json para obtener la lista de productos desde el archivo JSON.

    for producto in productos:  # Itero sobre cada producto en la lista de productos obtenida del JSON.
        inventory_page.agregar_producto_por_nombre(producto["nombre"])  # Llamo al método agregar_producto_por_nombre de InventoryPage para agregar el producto al carrito usando su nombre. AGREGA EL PRODUCTO POR NOMBRE, ACCEDIENDO AL VALOR DEL NOMBRE DEL PRODUCTO EN EL DICCIONARIO DEL JSON CON producto["nombre"].

    # VOY AL CARRITO
    inventory_page.ir_al_carrito()  # Llamo al método ir_al_carrito de InventoryPage para navegar a la página del carrito.
    
    # CAPTURO LOS PRODUCTOS DEL CARRITO
    productos_carrito = cart_page.obtener_productos_carrito()  # Llamo al método obtener_productos_carrito de CartPage para obtener la lista de productos actualmente en el carrito.

    for producto_json in productos:  # Itero sobre cada producto en la lista original de productos del JSON.
        encontrado = False  # Inicializo una variable encontrado como False para verificar si el producto está en el carrito.
        for producto_carrito in productos_carrito:  # Itero sobre cada producto en la lista de productos del carrito.
            if ( (producto_carrito["nombre"] == producto_json["nombre"]) and (producto_carrito["precio"] == producto_json["precio"])):  # Verifico si el nombre y precio del producto en el carrito coinciden con los del JSON.
                encontrado = True  # Si coinciden, establezco encontrado como True y salgo del bucle interno.
                break
        
        assert encontrado, f"Producto incorrecto o faltante: {producto_json['nombre']}"  # Hago una aserción para verificar que el producto fue encontrado en el carrito, si no, muestro un mensaje indicando cuál producto falta o es incorrecto.
