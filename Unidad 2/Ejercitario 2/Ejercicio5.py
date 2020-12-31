"""Leer un número y mostrar su cuadrado, repetir el proceso hasta que se
      introduzca un número negativo. """
print("Ingrese un numero")
numero=int(input())
while numero>=0:
      cuadrado=numero*numero
      print("su cuadrado es: ",cuadrado)
      numero=int(input("Ingrese un numero"))
else:
            print("el numero es negativo")