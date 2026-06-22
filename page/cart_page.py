from selenium.webdriver.common.by import By


class CartPage: # Defino la clase CartPage que representa la página del carrito de compras en la aplicación web. 
    def __init__(self, driver):
        self.driver = driver  # Iniciaza el navegador

        # Locators son las variables de los elementos de la página
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_items_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_items_price = (By.CLASS_NAME, "inventory_item_price")

    

    def obtener_productos_carrito(self):
        items = self.driver.find_elements(*self.cart_items)  # Obtiene una lista de elementos que representan los productos en el carrito utilizando el localizador cart_items.
        productos = []  # Crea una lista vacía llamada productos para almacenar la información de cada producto en el carrito.

        for item in items:  # Itera sobre cada elemento en la lista de items.
            nombre_item = item.find_element(*self.cart_items_name).text  # Para cada item, busca el elemento que contiene el nombre del producto utilizando el localizador cart_items_name y obtiene su texto.
            precio_item = item.find_element(*self.cart_items_price).text  # Para cada item, busca el elemento que contiene el precio del producto utilizando el localizador cart_items_price y obtiene su texto.

            productos.append(  # Agrega un diccionario a la lista productos con la información del nombre y precio del producto.
                    {
                        "nombre": nombre_item,
                        "precio": precio_item
                    }
            )

        return productos  # Devuelve la lista de productos con su nombre y precio.
