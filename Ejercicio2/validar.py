from tkinter import Tk,Button,Frame, messagebox, LabelFrame

class validacion():
    
    def __init__ (self):
        self.__usuario = "lala"
        self.__contraseña = "1234"
    
    def validar(self,user, contra):
        
        if (self.__usuario == user and self.__contraseña == contra):
            messagebox.showinfo("Exito","Bienvenido")
        else:
            messagebox.showerror("Error","Error no se puede ingresar")