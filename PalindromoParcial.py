'''La función de este programa es saber si el número introducido es palíndromo, o sea que si se lee de igual forma de derecha a izquierda como de izquierda a derecha.
por ejemplo: 32123, 434, 12321'''

print("")
n = int(input("Introduzca el valor a comprobar: "))  #Se introduce el número el cual se quiere saber si es palíndromo 
p = n #Guarda el valor de n introducido en otra variable, debido a que n luego va a variar
res = 0 #Es el valor en el cual se guardará el resultado volteado


while n > 0:  #Se inicia este algoritmo, el cual va a voltear el número 
    r = n % 10 #Guarda el último número actual en r
    n = n // 10 #Reduce el valor de n de forma entera 
    res = res * 10 + r # Es el resultado que nos dará el valor volteado
 
print("")
if res == p:  #Si el valor girado es igual al valor inicial, se sabe que es palíndromo 
    print ("Es palíndromo")
else:
    print("No es palíndromo")
