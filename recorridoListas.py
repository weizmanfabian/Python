
'''
hacer una empresa que tiene n empleados en n divisiones
cada empleado tiene un salario
solicitar cuales son las dependencias y cual es el salario
#determinar quien gana mas de cada dependencia
#quien gana mas de toda la empresa 
#determinar cuanto gana en total cada dependencia
determinar cuanto gana toda la empresa
investigar como calcular el valor maximo de una columna y de una matriz
'''


import functools


def pedir_entero(msg):
    return int(input(msg))


def elQueGanaMasPorCadaDependencia(arrayEmpresa):
    for departamento in arrayEmpresa:
        print(valorMasGrande(departamento))
        # salarioMasGrande = 0
        # for i, v in enumerate(arrayEmpresa):
        #     salarioMasGrande = v if v > salarioMasGrande else salarioMasGrande
        # print(salarioMasGrande)


def valorMasGrande(arrayDepartamento):
    return functools.reduce(lambda value, salarioMasGrande: value if value >
                            salarioMasGrande else salarioMasGrande, arrayDepartamento)


def sumaDeCadaDepartamento(arrayEmpresa):
    for departamento in arrayEmpresa:
        print(sumaDepartamento(departamento))


def sumaDepartamento(arrayDepartamento):
    return functools.reduce(lambda value, total: value + total, arrayDepartamento)


def elQueGanaMasDeTodaLaEmpresa(arrayEmpresa):
    salarioMasGrande = 0
    for depto in arrayEmpresa:
        salarioDepto = valorMasGrande(depto)
        salarioMasGrande = salarioDepto if salarioDepto > salarioMasGrande else salarioMasGrande
    return salarioMasGrande


def main():
    empresa = []
    departamentos = pedir_entero('Cuántos departamentos tiene la empresa')
    for x in range(departamentos):
        empresa.append(
            input('Escriba el nombre departamento ' + str(x + 1) + '\n'))

    print(empresa)

    for i, depto in enumerate(empresa):
        colaboradores = []
        cantidadEmpleados = pedir_entero(
            'Escriba cuántos empleados tiene el departamento ' + depto + '\n')
        for empleado in range(cantidadEmpleados):
            colaboradores.append(pedir_entero(
                'Escriba el salario del empleado ' + str(empleado + 1) + '\n'))
        empresa[i] = colaboradores

    for x in empresa:
        print(x)

    print('El que gana más por cada dependencia es:')
    elQueGanaMasPorCadaDependencia(empresa)
    print('El que más gana de toda la empresa es {}'.format(
        elQueGanaMasDeTodaLaEmpresa(empresa)))
    print('El total por cada dependencia es:')
    sumaDeCadaDepartamento(empresa)


main()
# lis = [[1, 12, 7], [3, 8, 1], [5, 7, 30], [6, 9, 1], [2, 9, 5]]
# elQueGanaMasDeTodaLaEmpresa(lis)
