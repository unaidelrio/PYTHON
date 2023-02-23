# texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."

# a = texto.replace("Pitón", "Python")
# b = a.replace("difícil", "fácil")
# c = b.replace("Bill Gates", "Guido van Rossum")
# d = c.replace("1960", "1991")
# print(d)


# texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil.        "

# textoFind = texto.find("Python")
# print(textoFind)
# print(texto[46:52])
# textoCount = texto.count("Python")
# print(textoCount)
# print()
# textoReplace = texto.replace("Python", "PYTHON") #reenplazar la palabra y hacerla mayusculas
# print()
# print(textoReplace)
# textoStrip = texto.strip() #Quitar espacios
# print(textoStrip)
# print()
# textoUpper = textoStrip.upper() #Hacer mayuscula todo el texto
# print(textoUpper)
# textoCountUpper = textoUpper.count("PYTHON")
# print(textoCountUpper)


# emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
# nombres = ""
# dominios = ""
# for i in emails:
#     nombre,dominio = i.split("@")
#     if "." in nombre:
#         aux1 = nombre.split(".")
#         nombre_completo= " ".join(i for i in aux1)
#     else:
#         nombre_completo = nombre
#     nombres = nombres+ "," + nombre_completo
#     if dominio not in dominios:

# repetido = [str(rep) for rep in texto if rep == "Python" or rep == "python"]
# print(repetido)
nombres = ("maria", "jon", "david")
texto = ",".join(nombre + @aulanz.net)