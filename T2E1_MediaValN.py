'''La función de este programa es, según el valor de n (enteros), va a pedir la misma cantidad de valores que n y va a sacar
el promedio de los valores pares dentro de los introducidos (en v)'''


n = int(input("introduzca número de enteros: "))
res = 0
p = 0
for i in range (n):
    v = int(input("Introduzca un valor: "))
    if v % 2 == 0:
        res = res + v
        p = p + 1
res = res / p 
print ("La media de los valores pares es {}".format(res))