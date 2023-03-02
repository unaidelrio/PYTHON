from common.nomUsuario import *

if __name__ == "__main__":
    usuario = get_usuario()
    edad = get_edad()
    contraseña = get_password() 

print(f"Bienvenido {usuario}. Tu edad es {edad} y tu contraseña es {contraseña}.")