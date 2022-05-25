# Un menu con 4 opciones +-*/ cada opción debe mostrar el error.
# En la opcion del menu, me tiene que decir opcion no validad si es un numero que sea diferente 1234
# y su es una letra o otra tipo de caracter me tiene que enviar un mje de error.
import operator


def calcular_operacion(num1, num2, operador, msg):
    resultado = operador(num1, num2)
    print(msg, resultado)


def pedir_numero(msg):
    num = int(input(msg))
    return num


def calcular(msg1, msg2, operador, msgFinal):
    numero1 = pedir_numero(msg1)
    numero2 = pedir_numero(msg2)
    calcular_operacion(numero1, numero2, operador, msgFinal)


def menu():
    print('-----------------------------------------------------')
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    try:
        opcion = int(input("Elija la opcion que desea ejecutar "))
        if opcion > 4 or opcion < 1:
            print("Opcion no valida")
            menu()
        elif opcion == 1:
            calcular('Escriba Sumando 1', "Escriba Sumando 2",
                     operator.add, 'El resultado de la suma es:')
        elif opcion == 2:
            calcular('Escriba el Minuendo', "Escriba el Sustraendo",
                     operator.sub, 'El resultado de la resta es:')
        elif opcion == 3:
            calcular('Escriba el Multiplicando', "Escriba el Multiplicador",
                     operator.mul, 'El resultado de la multiplicación es:')
        elif opcion == 4:
            calcular('Escriba el Dividendo', "Escriba el Divisor",
                     operator.truediv, 'El resultado de la división es:')
    except:
        print("Solo se aceptan numeros")

    repeat = int(
        input('Desea repetir 1=> Sí.\nDe lo contrario escriba otra letra'))
    if repeat == 1:
        menu()


menu()
