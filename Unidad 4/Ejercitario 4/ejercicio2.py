"""02) Escriba un programa que pida un número entero mayor que cero y que muestre en
pantalla sus divisores(agregar los divisores en una lista para luego imprimir en
pantalla) """
print("ingrese un numero entero")
numero=int(input())
while numero<0:
    print("debe ser mayor o igual a cero ingrese de nuevo")
    print("ingrese un numero entero")
    numero=int(input())
def divisores(numero):
    """
    Genera una lista de los divisores de un número.
    """
    resultado = [i for i in range(1, numero + 1) if numero % i == 0]

    return resultado

print(divisores(numero))

    
    



