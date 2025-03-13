print(" ")
n = int(input("Escriba un entero positivo: "))
cad = str(n)
salida = ""
fin = ""
if n > 0 :
    for i in range(n):
        if cad[i] == "0":
            salida = "0"
            fin = salida + fin
        else:
            salida = str(cad[i])
            fin = str(int(salida)+1) + fin
else: 
    print("ERROR: Introduzca un número entero positivo")
print(fin)