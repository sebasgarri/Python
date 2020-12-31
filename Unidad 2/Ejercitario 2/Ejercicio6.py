"""6. Dadas 6 notas, escribir la cantidad de alumnos aprobados y los no aprobados.
    (Aprobados mayores a 1)(No aprobados menor o igual a 1)."""
contadoraprobados=0
contadornoaprobados=0
for x in range(6):
   print("Ingrese la nota")
   nota=int(input())
   if nota>1:
       contadoraprobados=contadoraprobados+1
   else:
           contadornoaprobados=contadornoaprobados+1
print("La cantidad de aprobados es: ",contadoraprobados)
print("La cantidad de no aprobados es: ",contadornoaprobados)
