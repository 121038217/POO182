import string
import random
from tkinter import messagebox
class GenerarMatricula:
    def __init__(self, nombre, apellidoP, apellidoM, fechanacimiento, carrera,contr):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.fechanacimiento = fechanacimiento
        self.carrera = carrera
        self.contr = contr

    def generar_matricula(self):
        añoo = int(self.fechanacimiento.get())
        letranombre = self.nombre.get()
        letraapellidoM = self.apellidoM.get()
        letraapellidoP = self.apellidoP.get()
        carreraa = self.carrera.get()
        
        caracteres = string.ascii_lowercase
        if letranombre:
            caracteres += string.ascii_uppercase
        if letraapellidoM:
            caracteres += string.ascii_uppercase
        if letraapellidoP:
            caracteres += string.ascii_uppercase
        if carreraa:
            caracteres += string.ascii_uppercase
        
        pass1 = ''.join(random.choice(caracteres) for i in range(letranombre))
        self.contr.set(pass1)
        pass2 = ''.join(random.choice(caracteres) for i in range(letraapellidoP))
        self.contr.set(pass2)
        pass3 = ''.join(random.choice(caracteres) for i in range(letraapellidoM))
        self.contr.set(pass3)
        pass4 = ''.join(random.choice(caracteres) for i in range(añoo))
        self.contr.set(pass4)
        
        messagebox.showinfo("Matricula","La matricula generada es: " + pass1+pass2+pass3+pass4)
        
        