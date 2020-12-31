'''Escribir un programa que simule una calculadora y que contenga las siguientes funciones.
   Muestre un menú con 5 opciones:'''
from tkinter import *

vtn=Tk()
vtn.title=("Calculadora")
vtn.geometry('235x150')
vtn.configure(background="cyan")

def suma():
    suma=int(txt1.get())+int(txt2.get())
    return resultado.set(suma)
def resta():
    resta=int(txt1.get())-int(txt2.get())
    return resultado.set(resta)
def multiplicacion():
    multiplicacion=int(txt1.get())*int(txt2.get())
    return resultado.set(multiplicacion)
def division():
    division=int(txt1.get())/int(txt2.get())
    return resultado.set(division)
def cerrar():
    vtn.destroy()
resultado=StringVar()

lbl1 = Label(vtn,text="Primer número",bg='cyan',fg='black')
lbl1.grid(row=1,column=1)
txt1=Entry(vtn)
txt1.grid(row=1,column=2)

lbl2 = Label(vtn,text="Segundo número",bg='cyan',fg='black')
lbl2.grid(row=2,column=1)
txt2=Entry(vtn)
txt2.grid(row=2,column=2)

btnsuma=Button(vtn,text="+",bg="yellow",fg="black",width=11,command=suma)
btnsuma.grid(row=3,column=1)

btnresta=Button(vtn,text="-",bg="yellow",fg="black",width=11,command=resta)
btnresta.grid(row=3,column=2)

btnmulti=Button(vtn,text="*",bg="yellow",fg="black",width=11,command=multiplicacion)
btnmulti.grid(row=4,column=1)

btndivi=Button(vtn,text="/",bg="yellow",fg="black",width=11,command=division)
btndivi.grid(row=4,column=2)

btncerrar=Button(vtn,text="Cerrar",bg="red",fg="white",width=30,command=cerrar)
btncerrar.grid(row=5,column=1,columnspan=2)

lblres = Label(vtn,bg='white',width=30,textvariable=resultado)
lblres.grid(row=6,column=1,columnspan=2)

vtn.mainloop()