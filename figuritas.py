'''
Colección de Figuritas 

Una importante empresa de productos de comidas rápidas está desarrollando una aplicación para facilitar que sus clientes intercambien figuritas de objetos animados que dan por la compra de un combo infantil. Las figuritas se organizan por categoría según el tipo de figurita como accion, magia, animal, batalla y dios, la única restricción que pedirá la aplicación es que solo se pueden intercambiar por figuritas del mismo tipo.

Lo han contratado a usted y su función es desarrollar una librería llamada “figuritas” que permita realizar las siguientes funciones: 

1. (Vale 1) La función "tipodefigurita" que dada una lista de los tipos de figurita(en la posición i-ésima de la lista está el tipo de dicho figurita), genera una lista con los tipos de figuritas sin repetición.

Por ejemplo si el álbum tiene diez figuritas y cada una tiene los siguientes tipos:

['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla']

la función debe retornar la lista

['accion','magia','batalla']

Nótese que las clases aparecen solo una vez. 


2. (Vale 1) La función "mefaltandeltipodefigurita " que dada una lista con los números de figuritas que les faltan, la lista de los tipos de cada figurita y un tipo de figurita (en ese orden), les retorne una lista con los números de dicha clase que les faltan.

Por ejemplo si se ejecuta la función:

mefaltandeltipodefigurita([3,6,8],['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'],'batalla')


debe retornar la lista

[3,8]

Nótese que los números de figuritas empiezan en cero (0) y van hasta el nueve (9) en este ejemplo (siempre empiezan en cero).

Por ejemplo si ejecutan la

función:

mefaltandeltipodefigurita([1,3,6,8],['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'],'magia')  


Se debe retornar la lista:

[1,6] 


3. (Vale 1) La función "notengo" que dada una lista con las figuritas que tiene otra persona y una lista con las figuritas que tengo retorna la lista con las figuritas que me interesan de la otra persona.

Por ejemplo si se llama:

notengo([3,5,7,10,15,16],[4,10,5,8])

Se debe retornar la lista:

[3,7,15,16] 

4. (Vale 1) Para simplificar la primera versión de la librería decidieron pensar que todas las figuritas son de un mismo tipo y que la lista que maneja cada persona indica los números de las figuritas que tienen para cambiar y aquellos números que no están en dicha lista son los que necesitan. De esta manera deben crear una función "puedocambiar" que reciba la lista de figuritas que tiene otra persona y la lista de figuritas que tienen ellos y que retorne el número de figuritas que pueden cambiar.

Por ejemplo, llamar la función:

puedocambiar([3,5,7,10,15,16],[4,10,5,8])

Debe retornar

2

Porque a la otra persona solo le interesan dos figuritas que tienen ellos: [4,8], mientras que a ellos les interesan cuatro figuritas que la otra persona tiene: [3,7,15,16] 

Entrada:

Este programa no requiere entrada. Ni generará salida. Se requiere que el estudiante genere un archivo con el nombre figuritas.py y que se respeten los nombres de las funciones dadas y sus parámetros.


https://j2logo.com/python/tutorial/tipo-set-python/#:~:text=Al%20comienzo%20del%20tutorial%20adelantaba%20que%20el%20tipo,guardan%20ning%C3%BAn%20orden%20y%20que%20adem%C3%A1s%20son%20%C3%BAnicos.
'''
from functools import reduce


def tipodefigurita(lista):
    def func_auxiliar(acc, num):
        if num not in acc:
            acc.append(num)
        return acc
    return reduce(func_auxiliar, lista, list([]))


def mefaltandeltipodefigurita(posiciones, lista_figuras, nombre_figura):
    return [n for n in posiciones if lista_figuras[n] == nombre_figura]


def notengo(lista_persona1, lista_persona2):
    return [n for n in lista_persona1 if n not in lista_persona2]


def puedocambiar(lista1, lista2):
    repetidosLista1 = reduce(lambda acc, fig: acc +
                             1 if fig not in lista2 else acc + 0, lista1, 0)
    repetidosLista2 = reduce(lambda acc, fig: acc +
                             1 if fig not in lista1 else acc + 0, lista2, 0)
    return repetidosLista1 if repetidosLista1 < repetidosLista2 else repetidosLista2
