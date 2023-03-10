import tkinter as tk
import string
from tkinter import *
from tkinter import messagebox
from comprobar import *

ventana = Tk()
ventana.title(" Caja popular")
ventana.geometry("400x300")

seccion1=Frame(ventana,bg="#03c2fc")
seccion1.pack(expand=True,fill='both')

Nocuenta = tk.StringVar()
etiqueta1=Label(seccion1,text="No. de cuenta ")
etiqueta1.place(x=150,y=10)
caja1 = Entry(seccion1)
caja1.place(x=150,y=40)

titular = tk.StringVar()
etiqueta1=Label(seccion1,text=" Titular: ")
etiqueta1.place(x=150,y=10)
caja1 = Entry(seccion1)
caja1.place(x=150,y=40)

edad = tk.StringVar()
etiqueta1=Label(seccion1,text=" Edad: ")
etiqueta1.place(x=150,y=10)
caja1 = Entry(seccion1)
caja1.place(x=150,y=40)

saldo = tk.StringVar()
etiqueta1=Label(seccion1,text=" Saldo")
etiqueta1.place(x=150,y=10)
caja1 = Entry(seccion1)
caja1.place(x=150,y=40)



botonAceptar=Button(seccion1,text=" consultar saldo",bg="#7399bf",fg="black")
botonAceptar.place(x=100,y=60,width=100,height=30)

botonAceptar=Button(seccion1,text=" Ingresar efectivo",bg="#7399bf",fg="black")
botonAceptar.place(x=100,y=100,width=100,height=30)

botonAceptar=Button(seccion1,text=" Retirar efectivo",bg="#7399bf",fg="black")
botonAceptar.place(x=100,y=140,width=100,height=30)

botonAceptar=Button(seccion1,text=" Depositar",bg="#7399bf",fg="black")
botonAceptar.place(x=100,y=100,width=100,height=30)

ventana.mainloop()