import imp
import json
from jsonApi import consultar

# escribir diccionario en un python y en otro recibirlo

dataJson = consultar()
print(dataJson)
data = json.loads(dataJson)
print(data)
