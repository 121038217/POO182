from tkinter import *
from validar import validacion
import tkinter as tk 
                 
a = validacion()

def ejecuta():
        a.validar(et1.get(),et2.get())

ventana = Tk()
usuario = validacion()
ventana.title(" Login")
ventana.geometry("400x300")

seccion1=Frame(ventana,bg="#03c2fc")
seccion1.pack(expand=True,fill='both')

et1 = tk.StringVar()
etiqueta1=Label(seccion1,text=" Usuario ")
etiqueta1.place(x=150,y=10)
caja1 = Entry(seccion1)
caja1.place(x=150,y=40)

et2 = tk.StringVar()
etiqueta2=Label(seccion1,text=" Contraseña ")
etiqueta2.place(x=150,y=80)
caja2 = Entry(seccion1)
caja2.place(x=150,y=120)
caja2.config(show="*")

botonAceptar=Button(seccion1,text="Aceptar",bg="#7399bf",fg="black",comman=ejecuta)
botonAceptar.place(x=180,y=160,width=100,height=30)

ventana.mainloop()