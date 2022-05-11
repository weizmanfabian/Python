'''
Crear una matriz dinamica en la que guarde x numero de aprendices en x grados
'''
listaGeneral = []
num_filas = int(input('Ingrese la cantidad de filas'))
num_columnas = int(input('Ingrese la cantidad de columnas'))

for x in range(0, num_filas, 1):
    lista_interna = []
    for y in range(0, num_columnas, 1):
        entrada = input('Ingrese el nombre del Aprendiz ' +
                        str(y + 1) + ' de la fila ' + str(x + 1))
        lista_interna.append(entrada)
    listaGeneral.append(lista_interna)

for z in listaGeneral:
    print(z)

for i, v in enumerate(listaGeneral):
    for ind_hijo, v_hijo in enumerate(v):
        if i == ind_hijo:
            print(v_hijo)
