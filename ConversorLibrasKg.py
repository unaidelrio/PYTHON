sistema = input("elegir K si quieres kilos a libras L si quieres libras a kilos ")
numPeso = float(input("Introducir peso: "))
# kg = numPeso * 2.20462
# libras = numPeso / 2.20462

if sistema == ("K") or ("k"):
    # print(f"Tu peso en libras es {kg}")
    print(f"Tu peso en libras es {numPeso * 2.20462}")
elif sistema == ("L") or ("l"):
    # print(f"Tu peso en Kg es {libras}")
    print(f"Tu peso en Kg es {numPeso / 2.20462}")
else:
    print("Vuelve a intentarlo")