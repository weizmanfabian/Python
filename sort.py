# Realice un algoritmo o pseudo-código que permita ordenar de mayor a menor, cuatro números ingresados en cualquier orden. (no usar sort)

data = [3, 8, 9, 2]
respuesta = []
mayor = 0

for padre in data:
    mayorInterno = 0
    for hijo in data:
        if mayorInterno < hijo:
            if len(respuesta) == 0:
                mayor = hijo
                mayorInterno = hijo
                continue
            if hijo < mayor:
                mayorInterno = hijo
        if hijo == mayor:
            continue
    respuesta.append(mayorInterno)
    mayor = mayorInterno

print(respuesta)
