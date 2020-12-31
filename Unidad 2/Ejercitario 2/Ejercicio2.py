"""Pedir por teclado 10 números. Mostrar la media de los números positivos, la media de los
números negativos y la cantidad de ceros."""
contadorpositivo=0
contadornegativo=0
contadorcero=0
for x in range(10):
    print("Ingrese un numero")
    numero=int(input())
    if numero < 0 :
        contadornegativo=contadornegativo+1
    elif numero > 0 :
         contadorpositivo=contadorpositivo+1
    elif numero == 0 :
        contadorcero=contadorcero+1
print("La cantidad de numeros positivos es: ",contadorpositivo)
print("La cantidad de numeros negativos es: ",contadornegativo)
print("La cantidad de numeros ceros es: ",contadorcero)


    
       
