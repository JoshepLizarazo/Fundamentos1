'''La función de este programa es sumarle 1 a cada cifra de n, y si la cifra es 9 (Que por lo tanto 
la suma sería igual a 10), entonces la reemplaza con un 0'''

print(" ")
n = int(input("Escriba un entero positivo: "))
cad = str(n)
lg = len(cad)
salida = ""
fin = ""
if n > 0 :
    for i in range(lg):
        if cad[i] == "9":
            salida = "0"
            fin = fin + salida
        else:
            salida = str(cad[i])
            fin = fin + str(int(salida)+1) #Convierte el valor de salida a entero y le suma 1, luego se vuelve a convertir
                                            # en cadena para añadirlo a la string de "fin"
else: 
    print("ERROR: Introduzca un número entero positivo")
print("{} ---> {}".format(n, fin))