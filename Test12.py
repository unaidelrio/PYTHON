valido = False
password = input("¿Cual es tu contraseña? ")
while valido == False:

    lista = ["password", "contraseña", "123456"]
    if len(password)<=5:
        print("El nombre de usuario tiene que ser mayor que 5")
    if len(password)<=6:
        print("La contraseña tiene que ser mayor que 6")
    if valido == True:
        break
    else:
        password = input("¿Cual es tu contraseña? ")