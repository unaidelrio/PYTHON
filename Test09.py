s= "   122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  " 

s = s.strip() #quita los espacios
a = s.split(",") #separa los caracteres en forma de lista 
print(s)
print(a)
print(type(a)) #lista

# b = [] #creamos otra lista
# for i in a:
#     if not i.isnumeric(): #rastrea los numeros en la lista y los elimina
#         b.append(i)

b = [str(i) for i in a if not i.isnumeric()]
print(b)
finalT =""
finalT = " ". join(str(i) for i in b)
# for i in b:
#     finalT= finalT + i + " "
print(finalT)
print(finalT.upper())


