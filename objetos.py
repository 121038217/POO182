from personaje import * 
 
print("")
print("### Solicitud de Datos Heroe ###")
especieH= input("Ecribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH=float(input("Escribe la altura del Heroe: "))
recargarH=int(input("Ingresar las balas para el Heroe: "))

print("")
print("### Solicitud de Datos Villano ###")
especieV= input("Escribie la especie del villano: ")
nombreV= input("Escribe el nombre del villano: ")
alturaV=float(input("Escribe la altura del villano: "))
recargarV=int(input("Ingresa las balas para el villano: "))


#2.Creamos los objetos
Heroe = Personaje(especieH, nombreH, alturaH)
Villano=Personaje(especieV, nombreV, alturaV)

#3.Usamos los atributos del Heroe y Villano
print("")
print("### Atributos y Metodos del Heroe ###")
print("El personaje se llama "+Heroe.nombre)
print("pertenece a la especie "+Heroe.especie)
print("y una altura de "+ str(Heroe.altura))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargarH)

print("")
print("### Atributos y Metodos del Villano ###")
print("El personaje se llama "+ Villano.nombre)
print("pertenece a la especie "+ Villano.especie)
print("y una altura de "+ str(Villano.altura))

Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargarV)