'''
Este algoritmo detecta si el número introducido es equivalente a 
la raiz cuadrada entera de otro número
'''

print("")
n = int(input("introduzca el número: "))
print("")
raiz = n**(1/2)
if n < 0:
    print("")
    
    print("Error: Los negativos no pueden ser cuadrados enteros de un número real")
    print("")
elif raiz - int(n**(1/2)) == 0:
    print("")
    print ("{} es cuadrado entero de {}".format(n, raiz))
    print("")
else:
    print("")
    print ("{} no es cuadrado de ningún número entero".format (n))
    print("")