# import requests

# link = "http:/info.cern.ch/"
# r = requests.get(link)
# print(r.status_code) #la llamada de HTTP ha ido correctamente

# html = r.text



import os

# path = os.getcwd()
# print(os.listdir(path)) #muestra los archivos y el directorio
# print(type(path))

path = os.getcwd()
print(path)
os.chdir('../')
path = os.getcwd()
print(path)
