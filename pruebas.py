# for i in range(10):
#     print(i)
# for j in range(2, 20):
#     print(j)

# for i in range(5):
#     print("Hola")

# for i in range(5):
#     x = input("?")
#     print(x)

# for i in range(10):
#     print(f"bucle {i}")
    
# MAX = 10 #mayusculas para constantes
# for j in range(MAX):
#     #hacer algo aqui...

# for j in range(2, 20):
#     print(j)
# print()

# repetir = int(input("cuantas veces..."))
# for i in range(repetir, -1, -1):
#     print(repetir)

# gente = int(input("¿Cuanta gente?"))
# invitados = [] #crea una lista vacia para ir llenandola en el bucle (if)
# MAX_INVITADOS = 3 #Mayusculas por que el valor no va a cambiar

# if gente > MAX_INVITADOS:
#     print("Demasiada gente")
# else:
#     for i in range(gente):
#         nombre = input("Introducir un invitado ")
#         print(f"El invitado {i} es  {nombre}")
#         invitados.append(nombre) #añade un nombre a la variable lista
#     for i in invitados: #imprime los nombres inscritos en la variable lista de invitados
#         print(i)

# accion = print(input("Quieres salir?" "q"))

# while accion != "Quit" or "quit":



#ejercicio5
# def numbers():
#     return 10, 20, 30

# a = numbers()

# print(type(a))


# instrumentos = ["guitarra", "piano", "piano", "ukelele", "bateria"]
# print(instrumentos)
# #loop
# for instrumentos in instrumentos: #imprime la lista en horizontal
#     print(instrumentos)
# #length / longitud (imprime la lista de arriba abajo)
# print(len(instrumentos))
# #count() cuidado - no es el numero de objetos, sino la cuenta la cantidad de lo escrito en la lista
# print(instrumentos.count("piano"))
# #acceso
# print(instrumentos[0]) #imprime el numero 0 de la lista (guitarra)
# print(instrumentos[1]) #imprime el numero 1 de la lista (piano)
# print(instrumentos[-1]) #imprime el ultimo de la lista (bateria) en el caso de tener una lista extensa
# print(instrumentos[:3]) #imprime los primeros tres
# print(instrumentos[3:]) #imprime los ultimos 3
# print(instrumentos[1:3]) #imprime del 2 al 3
# #modificar
# instrumentos[2] = "PIANO" #modifica el numero 2 (3) de la lista
# #añadir
# instrumentos.append("BATERIA") #añade al final de la lista
# instrumentos.insert(2, "BAJO") #añade en el medio de la lista en este caso  en el 2
# #quitar
# instrumentos.remove("BATERIA") #elimina de la lista el primero 
# instrumentos.pop() #elimina el ultimo de la lista
# del(instrumentos) #elimina la lista entera
# #ordenar
# instrumentos.sort() #ordena tanto numericamente como alfabeticamente
# instrumentos.sort(reverse=True) #ordena al reves

# #lista con ()
# dias = ("Lunes", "Martes0") # se utiliza parentesis para una lista que no cambiaria, en el caos de una lista modificable mejor "[]"


# alumnos = []
# MAX = 10 
# for i in range(MAX):
#     alumno = input("Cual e stu nombre? ")
#     alumnos.append(alumno)


# from random import:

# help("modules")
# help("random")

import random  #para pode rutilizar random

# print(dir(random))
x = random.random()
y = random.randint(1,3)
frutas = ["Manzana", "Platano", "Kiwi"]
z = random.choice(frutas)

print(x)
print(f"{x:.2f}")
print(y)
print(z)