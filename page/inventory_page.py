from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver  # Iniciaza el navegador

        # Locators son las variables de los elementos de la página
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.filtro = (By.CLASS_NAME,"product_sort_container")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.contador_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")




    # def: en cada función se definen todas las acciones que se pueden realizar en la página de inventario.

    def obtener_titulo (self):
        return self.driver.title # Devuelve el título de la página utilizando el atributo title del controlador de Selenium. 



    def obtener_productos(self):
        return self.driver.find_elements(*self.inventory_items) 
                                        # el * es un puntero que apunta a una dirección donde está guardada la información del locator, es decir, el tipo de locator y el valor del locator. En este caso, apunta a la variable self.inventory_items, que contiene el locator para los elementos de inventario en la página. 


    
    def menu_visible(self):
        return self.driver.find_element(*self.menu_button).is_displayed()  # uso el método find_element para localizar el elemento del menú utilizando el locator self.menu_button, y luego utilizo el método is_displayed() para verificar si el elemento está visible en la página. Devuelve True si el elemento está visible, de lo contrario, devuelve False.



    def filtro_visible(self):
        return self.driver.find_element(*self.filtro).is_displayed()
    


    def agregar_producto_al_carrito(self):
        return self.driver.find_elements(*self.add_to_cart)[0]  # Devuelve el primer elemento de la lista. Se usa el método find_elements en plural, que devuelve una lista de elementos que coinciden con el locator self.add_to_cart. Luego, se accede al primer elemento de la lista utilizando el índice [0] para devolverlo.
        # Otra forma es: 
            # return self.driver.find_element(*self.add_to_cart).click()    # find_element en singular devuelve el primer producto que encuentra. Y se ejecuta el método click() para hacer clic en el botón de agregar al carrito.



    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.contador_carrito).text  # Devuelve el texto del elemento del contador del carrito utilizando el locator self.contador_carrito. Esto se hace utilizando el método find_element para localizar el elemento y luego accediendo a su propiedad text para obtener el texto que se muestra en el contador del carrito.

    
    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.nombres_productos)[0].text 
    
    
    def ir_al_carrito(self):
        return self.driver.find_element(*self.link_carrito).click()  # Utiliza el método find_element para localizar el elemento del enlace del carrito utilizando el locator self.link_carrito, y luego utiliza el método click() para hacer clic en ese enlace y navegar al carrito de compras.


    def agregar_producto_por_nombre(self,nombre_producto_json):
        productos = self.driver.find_elements(*self.inventory_items) # Obtengo una lista de elementos que representan los productos en la página de inventario utilizando el localizador inventory_items.
    
        for producto in productos: # Itero sobre cada producto en la lista de productos.
            nombre = producto.find_element(*self.nombres_productos).text # Para cada producto, busco el elemento que contiene el nombre del producto utilizando el localizador nombres_productos y obtengo su texto.

            if nombre == nombre_producto_json: # Comparo el nombre del producto con el nombre proporcionado como argumento (nombre_producto_json).
                producto.find_element(*self.add_to_cart_buttons).click() # Si el nombre coincide, busco el botón de agregar al carrito dentro del producto utilizando el localizador add_to_cart_buttons y hago clic en él para agregar ese producto al carrito.

                break # Después de agregar el producto al carrito, se rompe el ciclo for para evitar seguir buscando otros productos.
