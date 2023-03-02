def get_numero():
    numero = int(input("Introducir tu numero: "))
    return numero

def repNum(numero):
    for i in range(numero):
        repNum(int(numero))
    
    
    
if __name__ == "__main__":
    print("un programa para repetir un numro-")
    numero = get_numero()
    repNum(numero)