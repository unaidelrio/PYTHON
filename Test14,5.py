class Perro:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def Comer(self):
        print(f"{self.nombre} ya ha comido.")
    
    def Dormir(self):
        print(f"{self.nombre} ha dormido.")
    
    def Ladrar(self):
        print(f"{self.nombre} dice: ¡Wooooooof!")



#añadir perro a la lista
if __name__ == "__main__":
    
    miles = Perro("Miles", "Jack Russell Terrier", 4, 8)
    buddy = Perro("Buddy", "Dachshund", 3, 10)
    jack = Perro("Jack", "Bullgog", 6, 12)  
    jim = Perro("Jim", "Bulldog", 1, 18)

    Perros = [miles, buddy, jack, jim]
    
    choice = input("Quieres añadir un perro a la lista y/n: ")
    
    while choice == "y" or choice == "Y":    
        nombre = input("Introducir nombre: ")
        raza = input("Introducir raza: ")
        edad = input("Introducir edad: ")
        peso = input("Introducir peso: ")
        perro = Perro(nombre, raza, edad, peso)
        Perros.append(perro)
        print(f"El perro se llama {nombre} y es un {raza}. Tiene {edad} años y pesa {peso}.")
        for i in Perros:
            p





