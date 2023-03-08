from tkinter import Tk,Button,Frame, messagebox, LabelFrame
from string import ascii_letters,digits,punctuation
import secrets
#from pass import passm

class comp():
    def __init__ (self):
        
        #Lista con letras en minusculas y mayusculas
        self.__letters = ascii_letters
        
        #Nos dara la lista de los numeros
        self.__digits = digits
        
        #Nos dara los caracteres
        self.__punctuation = punctuation
       
        def letters(self):
            return self.__letters 
        
        def digits(self):
            return self.__digits
        
        def punctuation(self):
            return self.__punctuation
        
    def __init__(self,long):
        long = 8
        self.__contraseña = contraseña = ""
        
        for i in range(long):
            #choice es para elegir un elemento aleatorio
            contraseña += ' '(secrets.choice(contraseña))
            messagebox.showinfo("Exito",contraseña)