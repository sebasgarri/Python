"""Escriba un programa que pida un año y que muestre en pantalla si es bisiesto o no.
Condiciones para determinar cuándo un año es bisiesto.
1. Debe ser divisible entre 4.
2. No debe ser divisible entre 100.
3. Debe ser divisible entre 400 """

print("Ingrese el año para analizar")
fecha=int(input())
if fecha % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif fecha % 4 == 0 and fecha % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif fecha % 4 == 0 and fecha % 100 == 0 and fecha % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif fecha % 4 == 0 and fecha % 100 == 0 and fecha % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")

