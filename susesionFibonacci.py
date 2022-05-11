
calcularHasta = 9
n1, n2 = 0, 1
counted = 0
#La primera variable rastrea cuántos valores queremos calcular
#Las siguientes dos variables, n1 y n2, son los dos primeros elementos de la lista
#Necesitamos indicar estos valores, de lo contrario nuestro programa no sabría por dónde empezar. Estos valores cambiarán a medida que empecemos a calcular nuevos números

while counted < calcularHasta:
    print(n1);
    new_number = n1 + n2;
    n1 = n2;
    n2 = new_number;
    counted += 1;

#--------------------------------- 2 forma ----------------------------------
limite = int(input('Escriba la cantidad de veces que ejecutará la sucesión Fibonacci'))

def calculate_number(number):
	if number <= 1:
		return number
	else:
		return(calculate_number(number-1) + calculate_number(number-2))

for number in range(limite):
	print(calculate_number(number))