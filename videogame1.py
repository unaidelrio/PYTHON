# COMO un programador de videojuegos,
# QUIERO desarrollar un programa para
# que el usuario adivine un número
# PARA mostrarlo como prototipo de videojuego
# creado en Python
print("Bienvenido al juego de adivinar numeros.")
print("Adivina el numero del 1 al 100.")
print("Te aviso, ¡No será fácil!")
nombreUsuario = input("Antes de nada, ¿Cual es tu nombre? ")
print(f"Genial {nombreUsuario} ¡Buena suerte!")
import random #Crear un numero random que se asignara a la edad del usuario a adivinar
numero = random.randint(1,100) #saca un numero del 1 al 100 aleatorio que sera el que el usuario tiene que adivinar
# print(numero) ##printeo el numero del randomizador para saber cual es mientras pruebo el programa
numUsuario = int(input("Introduce un numero: ")) #creo una variable en la que se añadira el numero introducido por el

while numero != (numUsuario): #si el numero del bucle no es el mismo que ha añadido el usuario re repite
    print("¡Fallaste!")
    print("Prueba de nuevo.")
    print("Si quieres salir escribe Salir")
    cambioNum = input(f"Introduce un numero: ") #esta variable es la que va ha etsar preguntando al usuario el numero hasta que lo adivine
    numUsuario = cambioNum #reemplaza el numero añadido recientemente por el que acaba de meter el usuario
    if cambioNum == "Salir":
        numUsuario = numero
print("Has adivinado el numero")

