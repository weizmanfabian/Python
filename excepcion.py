from ast import Try


def suma():
    try:
        num = int(input('Ingrese un número'))
        num1 = int(input('Ingrese otro número'))
        suma = num + num1
    except Exception as ex:
        print('Error en la compilación')
        print(type(ex))
