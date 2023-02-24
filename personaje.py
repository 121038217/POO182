class Personaje: 
    
    #Agregamos el constructor del personaje (encapsular es con 2 guiones baj0)
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom 
        self.__altura= alt

    
    
    #Metodos
    def correr(self,status):
        if(status):
            print("El personaje " + self.__nombre +" Esta corriendo")
        else:
            print("El personaje " + self.__nombre +" se detuvo")
    
    def lanzarGranadas(self):
        print("El personaje " + self.__nombre + " lanzo granada")
        
    def recargarArma(self,municiones):
        cargador=10
        cargador=cargador+municiones
        print("El arma recargada tiene " + str(cargador) + " balas")
        
    #def __pensar(self):
        #print("estoy pensando..........")
        
 #Gets y  Sets para un correcto encapsulamiento
       
    def getEspecie(self):
        return self.__especie
    def setEspecie(self,esp):
        self__especie=esp
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nom):
        self.__nombre=nom
        
    def getAltura(self):
        return self.__altura
    def setAltura(self,alt):
        self.__altura=alt
        