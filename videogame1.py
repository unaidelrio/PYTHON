# COMO un programador de videojuegos,
# QUIERO desarrollar un programa para
# que el usuario adivine un número
# PARA mostrarlo como prototipo de videojuego
# creado en Python

print("Adivina el numero del 1 al 100")
import random #Crear un numero random que se asignara a la edad del usuario a adivinar
numero = random.randint(1,100) #saca un numero del 1 al 100 aleatorio que sera el que el usuario tiene que adivinar
# print(numero) ##printeo el numero del randomizador para saber cual es mientras pruebo el programa
numUsuario = input("Introduce un numero: ") #creo una variable en la que se añadira el numero introducido por el

while numero != int(numUsuario): #si el numero del bucle no es el mismo que ha añadido el usuario re repite
    cambioNum = input(f"Introduce un numero: ") #esta variable es la que va ha etsar preguntando al usuario el numero hasta que lo adivine
    numUsuario = cambioNum #reemplaza el numero añadido recientemente por el que acaba de meter el usuario
print("Has adivinado el numero")

