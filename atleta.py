'''
Juan es un atleta muy bueno y aplicado,
Pedro siempre está compitiendo con él, pero nunca lo alcanza y está Felipe que no es aplicado y por esta razón
siempre está  más atrás que los dos anteriores. Juan corre dos veces la velocidad de Pedro,
pero Juan siempre le aumenta 4 m/s al finalizar la competencia. La velocidad de Pedro y Juan juntas
supera 5 veces la velocidad de Felipe.
'''
velocidad_pedro = int(input('Escriba la velocidad de Pedro'))
# correo 2 veces la velocidad de Pedro, pero Juan siempre le Aumenta 4 m/s al finalizar la competencia
velocidad_juan = (velocidad_pedro * 2) + 4
# vel_juan + vel_pedro / 5
velocidad_felipe = (velocidad_juan + velocidad_pedro) // 5

'''
En el colegio se tienen determinados premios según las velocidades alcanzadas
- 0 y 20 uno de bonificación en la nota final.
- 21 y 40 dos de bonificación en la nota final.
- 41 y 79 tres de bonificación en la nota final.
- >= 80 cuatro de bonificación en la nota final.
'''
print("{} {} {}".format(velocidad_pedro, velocidad_juan, velocidad_felipe))
print('uno' if velocidad_felipe >= 0 and velocidad_felipe <= 20
      else 'dos' if velocidad_felipe >= 21 and velocidad_felipe <= 40
      else 'tres' if velocidad_felipe >= 41 and velocidad_felipe < 80
      else 'cuatro' if velocidad_felipe >= 80
      else 'NO pasa nada')
