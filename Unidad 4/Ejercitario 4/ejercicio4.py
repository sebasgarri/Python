"""04) Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Se desea
calcular el jornal diario de acuerdo con los siguientes puntos:
1. la tarifa de las horas diurnas es de 5 euros,
2. la tarifa de las horas nocturnas es de 8 euros,
3. caso de ser domingo, la tarifa se incrementará en 2 euros el turno diurno y 3
euros el turno nocturno.
"""
print("Para calcular la tarifa en horario diurno presione 1 o si es nocturno presione 2")
turno=int(input())
print("Ingrese la cantidad de horas trabajadas")
horas=int(input())
while horas<0:
    print("las horas deben ser mayor a 0")
    print("ingrese nuevamente las horas trabajadas")
    horas=int(input())
print("si es un dia de la semana presione 1,si es domingo presione 2")
dia=int(input())
if turno==1 and dia==1:
    salario=horas*5
    print("el salario es de ",salario)
    print("euros")
elif turno==2 and dia==1:
    salario=horas*8
    print("el salario es de ",salario)
    print("euros")
elif turno==1 and dia==2:
    salario=horas*7
    print("el salario es de ",salario)
    print("euros")
    
elif turno==2 and dia==2:
    salario=horas*11
    print("el salario es de ",salario)
    print("euros")

