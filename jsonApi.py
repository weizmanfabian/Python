import json


def consultar():
    lista = {
        "nombre": "weizman",
        "apellido": "Castañeda",
        "edad": 23
    }
    return json.dumps(lista)
