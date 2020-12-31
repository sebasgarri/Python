""" Escribir un programa que detecte si un número es primo o no. Un número
       es primo si sólo es divisible por sí mismo y por la unidad."""
print("Ingrese un numero")
numero=int (input())
if numero==7  or  numero == 5 or numero == 2 or numero == 3  :
    print("El numero es primo")
elif numero== 9 or numero%3==0:
    print("El numero no es  primo")
elif numero%2!=0 and numero%4!=0 and numero%5!=0 and numero%7!=0:
   print("El numero es primo")
else:
    print("El numero ingresado no es primo")








