from tkinter import *
from comprobar import comp
from pass import passm
import tkinter as tk 

a = comp()
def ejecutar():
        a.comprobar(long.get())
        
ventana = Tk()
ventana.title(" Password Automático")
ventana.geometry("400x300")

seccion1=Frame(ventana,bg="white")
seccion1.pack(expand=True,fill='both')

long = tk.StringVar
long=Label(seccion1,text=" Ingresar contraseña")
long.place(x=100,y=10)
caja1 = Entry(seccion1)
caja1.place(x=200,y=10)



botonComprobar=Button(seccion1,text="Comprobar",bg="#7399bf",fg="black",command=ejecutar)
botonComprobar.place(x=180,y=160,width=100,height=30)

ventana.mainloop()