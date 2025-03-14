'''La función de este programa es detectar si el número es positivo o negativo, y además, cuenta la cantidad de estos
y saca el promedio de los valores ya introducidos. El programa no se deja de ejecutar hasta que la entrada sea 0'''

fin = False
print(" ")
p = 0
ng = 0 
prop = 0
pron = 0  
while fin == False :
    print(" ")  
    n = int(input("Introduzca un número entero: "))
    if n > 0:
        print("{} es positivo".format(n))
        p = p + 1
        prop = prop + n
        print(" ")
    elif n < 0 : 
        print("{} es negativo".format(n))
        ng = ng + 1
        pron = pron + n 
        print(" ")
    elif n == 0 :
        print(" ")
        print("Cero introducido") 
        fin = True
    if p > 0 :
        print(" ")
        print("Positivos: {}  prom: {}".format(p,prop/p))
    else:
        print(" ")
        print("Positivos: 0  prom: 0")
    if ng > 0:
        print("Negativos: {}  prom: {}".format(ng,pron/ng))
    else :
        print("Negativos: 0  prom: 0")     

print (" ")
print ("Fin del programa")
   
    
    
    