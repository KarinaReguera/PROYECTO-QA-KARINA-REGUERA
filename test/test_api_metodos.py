import requests

import pytest


#free_user_3EXtK4ArSiWNB7bOQKQ086N12rb

headers = {
    "x-api-key": "free_user_3EXtK4ArSiWNB7bOQKQ086N12rb"
}





# GET: consultar un usuario específico
# response = requests.get("https://reqres.in/api/users/2", headers=headers)
# hago una solicitud GET a la URL de la API para obtener información del usuario con ID 2 y la guardo en la variable "response". Acompaño a la solicitud con la clave "headers=headers".




# POST: crear un nuevo usuario
# body = {
#     "name": "John Doe",
#     "job": "Software Developer"
# }   

# response = requests.post("https://reqres.in/api/users", headers=headers, json=body)



# PUT: actualizar/REEMPLAZA un usuario existente 
# body = {
#     "name": "Ana Smith",
#     "job": "Lead developer"
#} 

#response = requests.put("https://reqres.in/api/users/2", headers=headers, json=body)




# PATCH: actualizar parcialmente un usuario existente
#body = {
#    "name": "Ana Rodriguez"
#} 

#response = requests.patch("https://reqres.in/api/users/2", headers=headers, json=body)




# DELETE: BORRAR un usuario existente

response = requests.delete("https://reqres.in/api/users/2", headers=headers)



print(response.status_code)

# print(response.json())  



