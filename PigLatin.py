#Se escogió la forma de PigLatin que cambia la primera consonante o grupo de consonantes al final y le añade un "ay" para formar una nueva palabra#


palabra = str(input("Introduzca la palabra a convertir: "))
n = len(palabra)
frase = ""
r = ""

for i in range (n):
    if i == 0:
        r = palabra[i]
    else:
        frase = frase + palabra[i]
frase = frase + r + "ay"
print (frase)



        