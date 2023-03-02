import os 

print(os.name)
print(os.uname())

print(os.getcwd())

path = os.path.join(os.getcwd(), "carpeta")
print(path)