"""ingresar tres edades,decir cual es el mayor"""
print("Ingrese la edad de jose")
edad1=int(input())
print("Ingrese la edad de martin")
edad2=int(input())
print("ingrese la edad de pedro")
edad3=int(input())
if edad1>edad2 and edad1>edad3:
    print("jose es el mayor")
elif edad2>edad1 and edad2>edad3:
        print("martin es el mayor")
elif edad3>edad1 and edad3>edad2:
        print("pedro es el mayor")        
        
