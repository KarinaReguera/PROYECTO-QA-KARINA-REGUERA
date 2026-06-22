import csv
import json

# lector del csv de usuarios: Lee un archivo CSV y devuelve una lista de tuplas para usar en parametrización de pytest
def read_user_csv():
    with open("data/users.csv", newline="") as file: # abre un archivo y le paso su ubicación "data/users.
                                # el parametro newline="" es para evitar las lineas vacias en el archivo csv
                                # lo defino como archivo "as file" para poder usarlo dentro del bloque with

        reader = csv.DictReader(file)   # lo converto en diccionario y lo guardo en "reader"

        return list(reader) # lo convierto en una lista y lo retorno
                            # queda un diccionario dentro de una lista, cada diccionario representa una fila del csv



# lector del json de productos: Lee un archivo JSON con información de productos y devuelve un diccionario con los datos de los productos.
def read_product_json():
    with open("data/products.json") as file: # abre un archivo y le paso su ubicación "data/products.json"
                                # lo defino como archivo "as file" para poder usarlo dentro del bloque with

        return json.load(file)  # lo convierto en un diccionario y lo retorno
    

        #OTRA FORMA DE HACERLO:
        #data = json.load(file)  # lo convierto en un diccionario y lo guardo en "data"

        #return data["products"]  # retorno la lista de productos que se encuentra dentro del diccionario "data"
    
