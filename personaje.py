class Peronaje:
    
    #Atributos
    especie="Humanos"
    nombre="Master"
    altura=2.70
    
    
    #Metodos
    def correr(self,status):
        if(status):
            print("El personaje " + self.nombre +" Esta corriendo")
        else:
            print("El personaje " + self.nombre +" se detuvo")