'''
Este algoritmo detecta si el número introducido es equivalente a 
la raiz cuadrada de otro número
'''


n = int(input("introduzca el número: "))
raiz = n**(1/2)
if n < 0:
    print("Error: Los negativos no pueden ser cuadrados enteros de un número real")
elif raiz - int(n**(1/2)) == 0:
    print ("{} es cuadrado entero de {}".format(n, raiz))
else:
    print ("{} no es cuadrado de ningún número entero".format (n))
