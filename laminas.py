'''
Hugo, Paco y Luis están coleccionando las láminas Locombia Tierra Querida y encontraron una tienda donde vende algunas láminas, 
cada lámina es vendida a un cierto precio. Como ellos tienen una lista con los códigos de las láminas que les hacen falta, 
quieren saber los códigos de las láminas que pueden comprar y el precio a pagar por dicha compra. 
Realizar un programa que dado un diccionario (en formato JSON) que tiene las parejas código:precio de todas las láminas 
que tiene la tienda, y que dada la lista de códigos de láminas que les faltan a Hugo, 
Paco y Luis (separados por espacios), imprima el precio de las láminas que pueden comprar y los códigos  de las láminas que pueden comprar:

Entrada
{"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}

d p h u i e t q

Salida
290

d u t q

'''

import json
entradaJson = str(input(''))
codigos = str(input(''))
diccionario = json.loads(entradaJson)
codigosLaminas = codigos.split(' ')
total = 0
output = ''
for codigo in codigosLaminas:
    if codigo in diccionario:
        total += diccionario[codigo]
        output += ' ' + codigo

print(total)
print(output)
