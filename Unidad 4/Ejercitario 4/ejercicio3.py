"""03) Escribir una función que calcule el factorial de un número. Por ejemplo, 5! = 5*4*3*2*1
= 120. """
print("ingrese un numero entero")
numero=int(input())
factorial=1
while numero<0:
    print("debe ser mayor o igual a cero ingrese de nuevo")
    print("ingrese un numero entero")
    numero=int(input())
for i in range(numero):
    factorial=factorial*numero
    numero=numero-1
print("el factorial del numero es",factorial)