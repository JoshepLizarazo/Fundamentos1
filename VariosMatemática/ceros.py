#Este algoritmo introduce ceros en medio de cada cifra en un número

from turtle import delay


n = int(input("Introduzca número: "))
nback = n
i = 0
factor = 1
while n > 0 :
    r = n % 10
    n = n // 10
    delay (1000)   
    i = i + factor * r
    factor = factor * 100
    print ("Valor actual r: " + str(r) + " valor actual n: " + str (n) + " Valor de I: " + str (i))
print (str (nback) + " ---> " + str (i))
print (f"{nback}  --->  {i}")
print ("{} --->  {}".format(nback, i))


