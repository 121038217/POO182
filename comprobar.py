import string
import random
from tkinter import messagebox

class caja:
    def __init__(self,Nocuenta,titular,edad,saldo):
        self.Nocuenta = Nocuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        
    def consultar_saldo(self):
        saldo = int(self.saldo.get())
        messagebox.showinfo("Saldo","El saldo es: " + saldo)
        print(messagebox.askyesno(message="¿Desea continuar?", title="Continuar"))
    
    def ingresar_efectivo(self):
        efectivo = int(self.saldo.get())
        messagebox.showinfo("Efectivo","El saldo es: " + efectivo)
        
    def retirar_efectivo(self):
        retirar = int(self.saldo.get())
        Label = messagebox.askquestion("pregunta",)
        messagebox.showinfo("Saldo","El saldo es: " + saldo)
        
    
        
        
        