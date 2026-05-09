# Selectors Proyecto

## Login Page
- Input Usuario: #user-name (id del campo de texto para usuario)
- Input Contraseña: #password (id del campo de texto para contraseña)
- Input Botón de Login: #login-button (id del campo de entrada tipo submit)
- Mensaje de error: [data-test: "error"] - .error-message-container h3 (Subtítulo con el mensaje de error)

## Inventory Page
- Contenedor de todos los productos: #inventory_container (id del contenedor general de todos los productos del inventario)
- Contenedor lista de productos: [data-test: "inventory_list"] - .inventory_list (contenedor de la lista de todos los productos)
-Contenedor de un producto: [data-test: "inventory_item"] -  - .inventory_item (contenedor de un producto)
- Contenedor imagen del producto: .inventory_item_img (contenedor de la imagen del producto)
- Contenedor de la descripción del producto: [data-test: "inventory_item_descr"] - .inventory_item_descr (contenedor de la descripción del producto)
- Contenedor Título del producto: [data-test: "inventory_item_name"] - .inventory_item_name (título del producto)
- Contenedor Precio del producto: [data-test: "inventory_item_price"] - .inventory_item_price (precio del producto)
- Botón Add to Cart:#add-to-cart (id del botón Add tu Card)
- Botón Remove: #remove (id del botón Remove)

## Cart
- Contenedor imagen carrito: #shopping_cart_container (contenedor imagen carrito)
- Cantidad productos en carrito: [data-test: "shopping-cart-badge"] (cantidad productos en carrito)
- Link carrito: [data-test: "shopping-cart-link"]
- Botón Continue Shopping: [data-test: "continue-shopping"] 
- Botón Checkout: [data-test: "checkout"]

## Filter
- Contenedor filtro: [data-test: "product_sort_container"] (contenedor imagen del filtro)

## Burger menu
- Botón hamburguesa del menú: [data-test: "react-burger-menu-btn"]
- Imagen hamburguesa del menú: [data-test: "open-menu"]
- Opción "All Items" del menú: #inventory_sidebar_link
- Opción "About" del menú: #about_sidebar_link
- Opción "Logout" del menú: #logout_sidebar_link
- Opción "Reset App State" del menú: #reset_sidebar_link


