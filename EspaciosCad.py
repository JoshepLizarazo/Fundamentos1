palabra = str(input("Introduzca frase a separar: "))
n = len(palabra)
salida = ""
for i in range(n):
    if palabra[i] == " ":
        print(salida)
        salida = ""
    else:
        salida = salida + palabra[i]
print (salida) #se imprime la última palabra que el "for" no toma en cuenta            
        
        
