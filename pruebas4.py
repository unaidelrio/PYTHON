import requests

link = "http:/info.cern.ch/"
r = requests.get(link)
print(r.status_code) #la llamada de HTTP ha ido correctamente

html = r.text