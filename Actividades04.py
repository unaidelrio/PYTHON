#opcion1
# import this

# print(this.c)
# print(this.s)

#opcion2
# import this as t

# print(t.c)
# print(t.s)

#opcion3
# from this import c,s

# print(c)
# print(s)


import requests

currency = "eur"
basecurrency = "aud"
url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"

resp = requests.get[url]

print(resp.text)
print(resp.json())


