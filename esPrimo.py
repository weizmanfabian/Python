# [on_true] if [expression] else [on_false] => operator ternary

numeroIngresado = int(input("ingrese un numero: "))


def esPrimo(numeroIngresado):
    contador = 0
    for num in range(1, numeroIngresado + 1, 1):
        contador = 1 if numeroIngresado % num == 0 else contador

    print("El Numero ", numeroIngresado,
          " es " if contador == 2 else " NO ", " primo ")


esPrimo(numeroIngresado)
