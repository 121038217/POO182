class Personaje:
    
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
    
    def lanzarGranadas(self):
        print("El personaje " + self.nombre + "lanzo granada")
        
    def recargarArma(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("El arma recargada tiene " + cargador + "balas")