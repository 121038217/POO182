import string
import random
from tkinter import messagebox
class GenerarMatricula:
    def __init__(self, nombre, apellidoP, apellidoM, fechanacimiento, carrera):
        self.nombre = nombre
        self.apellidoP = apellidoM
        self.apellidoM = apellidoM
        self.fechanacimiento = fechanacimiento
        self.carrera = carrera

    def generar_matricula(self):
        año = int(self.fechanacimiento.get())
        letra = self.nombre.get()
        
        caracteres = string.ascii_lowercase
        if letra:
            caracteres += string.ascii_uppercase
        
        letraa = ''.join(random.choice(caracteres) for i in range(letra))
        self.contr.set(letraa)
        añoo = ''.join(random.choice(año) for i in range(letra))
        self.contr.set(año)
        messagebox.showinfo("Contraseña","La contraseña generada es: " + añoo+letraa)
        
        