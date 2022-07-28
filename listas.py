'''
Crea una función metodosdearreglo() que a partir de la lista llamada arreglo, con lo elementos que se encarnan realice las siguientes tareas sin operación es al original:

• Borrar los elementos duplicados. 
• Borrar los elementos negativos. 
• Ordenar la lista de mayor a menor. 
• Eliminar todos los números impares. 
• Elevar a dos todo los números restante. 
• Realizar una suma de todos los números que quedan. 
• Añadir como primer elemento de la lista la suma realizada. 
• Devolver la lista modificada. 
• Finalmente, después de ejecutar la función, verifica si la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así: Ejemplo de verificación(En el caso que sea igual la suma debe imprimir True de lo contrario debe imprimir False)
'''


arreglo = [70, -40, 60, 17, -1, 43, -9, 12, -9, 12, -12, 5, -12, 5]


def metodosdearreglo(arreglo):
    sinDuplicados = list(Set(arreglo))
    print(sinDuplicados)


metodosdearreglo(arreglo)
