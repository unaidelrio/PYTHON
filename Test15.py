class vehiculo:

    def __init__(self, marca, modelo, typeFuel, actualFuel, maxFuel):
        self.marca = marca
        self.modelo = modelo
        self.typeFuel = typeFuel
        self.actualFuel = actualFuel
        self.maxFuel = maxFuel
        self.accidente = False

    def conducir(self):
        print(f"Estas conduciendo el {self.marca} {self.modelo}.")
        self.actualFuel = -1
        
        if self.actualFuel == 0:
            self.llenarDeposito
            
            
    def llenarDeposito(self):
        
        print(f"Tu {self.marca} está sin combustible, llena el deposito.")
        repostar = input("Quieres repostar y/n? ")
        if repostar.upper == "y":
            self.actualFuel = self.maxFuel
            self.conducir
        else:
            self.depositoVacio
            
                
    def chocar(self):
        self.accidente = True
        print("¡Chocaste!")
        self.averiado

    def averiado(self):
        print("Tu vehiculo se ha averiado.")
    
    def depositoVacio(self):
        print(f"No puedes conducir tu {self.marca} ya que no quieres repostar.")
        self.llenarDeposito    
                    
                    
           
        
#Vehiculos a elegir
if __name__ == "__main__":
    Toyota = vehiculo("Toyota", "Supra", "Gasolina", 10, 30)
    Nissan = vehiculo("Nissan", "Patrol", "Diesel", 20, 40)
    Ford = vehiculo("Ford", "Bronco", "Diesel", 0, 30)
    Peugeot = vehiculo("Peugeot", "205 GTI", "Gasolina", 10, 20)
    print("Elija su vehiculo:\n\n-Toyota\n-Nissan\n-Ford\n-Peugeot\n")
    choiceDrive = input("¿Qué coche quieres elegir? ")
    
    
    

    

