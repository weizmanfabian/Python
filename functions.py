
def primosDel1Al100():
    for numGeneral in range(0, 101, 1):
        esDivisible = 0
        for numValidate in range(1, numGeneral + 1, 1):
            esDivisible = esDivisible + 1 if numGeneral % numValidate == 0 else esDivisible
        print("El Numero ", numGeneral,
              " es " if esDivisible == 2 else " NO ", " primo ")


def paresEImpares1Al100():
    for num in range(0, 101, 1):
        print('el número ', num, ' es ' if num % 2 == 0 else 'NO es', ' par')


def question(option):
    if option == 1 or option == 2:
        primosDel1Al100() if option == 1 else paresEImpares1Al100(
        ) if option == 2 else 'Opción Inválida'
        desicion = int(input('Desea repetir el programa\n1 => Sí\n2 => No'))
        print('' if desicion ==
              1 else 'Gracias por utilizar este maravilloso programa. See you later')
        main() if desicion == 1 else 'Gracias por utilizar este maravilloso programa. See you later'
    else:
        print('Opción Inválida')
        main()


def main():
    print('Por favor ingrese la opción a ejecutar')
    opcion = int(
        input('1 => Primos y no primos del 1 al 100\n2 => Pares e impares del 1 al 100'))
    question(opcion)


main()
