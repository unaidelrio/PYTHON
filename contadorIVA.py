print("Bienvenido al conversor de IVA")
opcion = input("Para sumar escriba Sumar, para restar escriba Restar: ")
 
if opcion == "Sumar" or opcion == "sumar":
    pSinIVA = float(input("Introducir precio sin IVA: "))
    porcentaje = int(input("Introducir porcentaje: "))
    IVA = pSinIVA * (porcentaje / 100)
    print(f"Precio sin IVA: {pSinIVA}")
    print(f"IVA: {IVA: .2f}")
    print(f"Precio con IVA: {(pSinIVA + IVA): .2f}")

elif opcion == "Restar" or opcion == "restar":
    pIVA = float(input("Introducir con IVA: "))
    porcentaje = int(input("Introducir porcentaje: "))
    IVA = pIVA / ((porcentaje + 100) / 100)
    print(f"Precio sin IVA: {(pIVA - IVA): .2f}")
    print(f"IVA: {IVA: .2f}")
    print(f"Precio con IVA: {pIVA: .2f}")
else:
    print("Vuelve a intentarlo")