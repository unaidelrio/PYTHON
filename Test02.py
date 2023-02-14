a = 10
if a > 10 :
    print(f"la variable con valor{a} es mas qye 10.")
else:
    print(f"la variable con valor{a} es menor o igual a 10")

# cambiar el codigo para que el resultado es:
# b = -1
# b = 150
# b = 100
b = int(input("Introducir un valor:")) #dejar que el usuario introduzca un valor cualquiera.
if b < 100: #la variable b con valor -1 es menor que 100.
    print(f"la variable b con valor {b} es menor que 100.")
elif b > 100: #la variable b con valor 150 es mayor que 100.
    print(f"la variable b con valor {b} es mayor que 100.")
elif b >= 100: #la variable b con valor 100 es mayor igual al 100.
    print(f"la variable b con valor {b} es mayor igual que 100.")
