'''
ArpaLlanera Hero Pro

James Hammett y Kirk Hetfield ya están en Colombia, y su juego ArpaLlanera Hero ha sido todo un éxito. Sin embargo, el juego se les está haciendo un poco predecible y repetitivo, así que deciden consultar a Cliff Newsted y a Lars Trujillo por alguna idea innovadora para sacar la versión Pro del video juego. Éstos deciden sentarse a estudiar escalas y entrenar el oído musical, y se les ocurre una variación del juego para hacerlo más entretenido.

La dinámica del nuevo componente es la siguiente: en el juego van a sonar una serie de cuerdas, una cuerda a la vez, y cada cuerda asociada a una letra distinta del alfabeto; lamentablemente, el sonido algunas veces no suena con calidad perfecta, así que el sonido de la cuerda puede llegar representado por la letra del alfabeto en minúscula o en mayúscula. La idea es que la persona luego de escuchar la sucesión de sonidos, determine en primera instancia cuál cuerda sonó y cuántas veces sono la misma cuerda de manera consecutiva.

Un ejemplo sencillo de ésta dinámica se puede hacer con la canción “Master of Python”, que inicia con la secuencia: E,E,e,E,E,d,E,E,D,c,C. En este caso, los sonidos inferidos serán E (con cinco repeticiones), D (con una repetición), E (con dos repeticiones), D (con una repetición), y C (con dos repeticiones).

Como usted cumple ahora dos roles, "jalacables" y programador, decide construir un programa que resuelve la extensión propuesta. En este caso, usted va a hacer un programa que recibe la sucesión de cuerdas que está escuchando (y adivinando) el jugador, que puede estar en minúscula o en mayúscula, y cada sonido separado por coma. La salida debe ser en primera instancia la sucesión de cuerdas, representadas en mayúscula, sin tener en cuenta los sonidos repetidos, y debajo de cada cuerda, la cantidad de veces que sonó esta de manera consecutiva.

Entrada

La entrada consta de una sucesión de caracteres separados por coma que corresponden a las cuerdas asociadas a los sonidos determinados por el jugador.

Salida

La salida consta de dos líneas: la primera es la sucesión de sonidos de cuerdas sin repeticiones, en mayúscula y separadas por espacio; la segunda es la cantidad de veces que se repitió cada sonido de cuerda de manera consecutiva, separado también por espacio.

Entrada
E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E

Salida
E D E D C E B E A E A E G E G E F E

5 1 2 1 2 2 1 2 1 1 1 1 1 1 1 1 1 1

'''

from collections import OrderedDict
from timeit import repeat

entrada = str(input(''))

# formateo la entrada ['E', 'E', 'e', 'E', 'E', 'd', 'E', 'E', 'D', 'c', 'C', 'E', 'E', 'B', 'E', 'E', 'a', 'E', 'A', 'E', 'g', 'E', 'G', 'E', 'f', 'E']
entradaFormateada = entrada.split(',')
# print(entradaFormateada)

# convierto la entrada a mayusculas recorriendo con la función map y la funcion lambda. La combierto a list para que se deje acceder por el indice
entradaUpperCase = list(map(lambda x: x.upper(), entradaFormateada))
# verifico que todas las letras esten es mayusculas
print(entradaUpperCase)

# hago un select disctinc de las letras del contenido del array convertido a mayuscula y las agrego a la data
# data = list(OrderedDict.fromkeys(entradaUpperCase))

listaTemporal = []
contadorDiferentes = 0

for x in range(len(entradaUpperCase)):
    if x > 0:
        # print(listaTemporal[contadorDiferentes-1][0])
        if listaTemporal[contadorDiferentes-1][0] == entradaUpperCase[x]:
            # print(listaTemporal[contadorDiferentes-1][1])
            listaTemporal[contadorDiferentes -
                          1][1] = listaTemporal[contadorDiferentes-1][1] + 1
        else:
            #print("no es =")
            listaTemporal.append([entradaUpperCase[x], 1])
            contadorDiferentes += 1
    else:
        listaTemporal.append([entradaUpperCase[x], 1])
        contadorDiferentes += 1

listaNotasMusicales = ''
listaCantidadNotasMusicales = ''

for x, y in listaTemporal:
    listaNotasMusicales += ' ' + x
    listaCantidadNotasMusicales += ' ' + str(y)

print(listaNotasMusicales)
print(listaCantidadNotasMusicales)

# print(contadorDiferentes)
# print(listaTemporal)


# cuento cuantas veces está cada letra
# arrayValue = []
# for x in range(0, len(entradaUpperCase), 1):

#     arrayValue.append()
#     repeat = True
#     contador = 0
#     while repeat:
#         contador += 1
#         if entradaUpperCase[ip] != entradaUpperCase[ip + 1]:
#             repeat = False
#     arrayValue

# print(newData)
