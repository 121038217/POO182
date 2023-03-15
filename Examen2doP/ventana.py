from tkinter import *
from tkinter import ttk
import tkinter as tk 
from Clase import *

ventana = Tk()
ventana.title(" generar matricula")
ventana.geometry("600x500")

seccion1=Frame(ventana,bg="#03c2fc")
seccion1.pack(expand=True,fill='both')

nombre = tk.StringVar()
etiqueta1=Label(seccion1,text=" nombre ")
etiqueta1.place(x=150,y=10)
nombre = Entry(seccion1)
nombre.place(x=150,y=40)

apellidoP = tk.StringVar()
etiqueta2=Label(seccion1,text=" apellido paterno ")
etiqueta2.place(x=150,y=80)
apellidoP = Entry(seccion1)
apellidoP.place(x=150,y=120)

apellidoM = tk.StringVar()
etiqueta3=Label(seccion1,text=" apellido materno ")
etiqueta3.place(x=150,y=150)
apellidoM = Entry(seccion1)
apellidoM.place(x=150,y=190)

fechanacimiento = tk.IntVar()
etiqueta4= Label(seccion1,text=" fecha nacimiento")
etiqueta4.place(x=150,y=230)
largoo = tk.StringVar(value="4")
fechanacimiento = Entry(seccion1,textvariable=largoo)
fechanacimiento.place(x=150,y=260)

carrera = tk.StringVar()
etiqueta5= Label(seccion1,text=" carrera")
etiqueta5.place(x=150,y=290)
carrera = Entry(seccion1)
carrera.place(x=150,y=320)

contr = tk.StringVar()
passw = tk.Entry(ventana, textvariable=contr)
passw.pack()

gen = GenerarMatricula(nombre, apellidoP, apellidoM, fechanacimiento, carrera,contr)
botonAceptar=Button(seccion1,text="Aceptar",bg="#7399bf",fg="black",command=gen.generar_matricula)
botonAceptar.place(x=150,y=350,width=100,height=30)

ventana.mainloop()