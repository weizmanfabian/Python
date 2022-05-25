import json
cantidad_alumnos = int(input('Cantidad de alumnos: '))
#dic = {"nombre":"","apellido":"","documento":"","salon":""}
dic = []
for i in range(cantidad_alumnos):
    nombre = input('Nombre alumno: ')
    apellido = input('Apellido: ')
    documento = input('documento de identidad: ')
    curso = input('Salon de clase ')
    dic.append({
        "nombre": nombre,
        "apellido": apellido,
        "documento": documento,
        "salon": curso})
for i, j in enumerate(dic):
    print(str(i+1))
    print(j)

eleccion = int(input('Cual desea Eliminar'))
del dic[eleccion-1]
print(dic)
