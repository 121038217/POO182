from tkinter import Tk,Button,Frame,messagebox

#1. Generar una ventana
ventana = Tk()
ventana.title(" Ejemplo de 1 Frames")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1=Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

