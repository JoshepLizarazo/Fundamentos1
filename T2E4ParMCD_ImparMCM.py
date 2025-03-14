'''La función de este programa es detectar si los dos valores son pares, impares, o uno par e impar. Dependiendo si ambos
son pares o impares, saca el máximo común divisor, y si uno es par y el otro impar, entonces saca el mínimo común múltiplo'''


print("")
n = int(input("Introduzca el primer valor: "))
print("")
m = int(input("Introduzca el segundo valor: "))
res = 0 
maxx = 0 
comp = False


while comp == False:
    
    if n < 0 or m < 0:
        if n < 0 and m < 0:
            n = n*-1
            m = m*-1
            comp = True
        elif n < 0 :
            n = n*-1
            comp = True 
        else:
            m = m*-1
            comp = True 
    else:
        comp = True

if n == m :
        res = n
        print ("El máximo común divisor es: {}".format(res))
    
elif n % 2 == 0 and m % 2 == 0 : #Si ambos valores son par
    if n == 0 or m == 0:
        print ("El máximo común divisor es: 0")  
                 
    elif n < m :
        for i in range (1,m):
            if n % i == 0 and m % i == 0:
                res = i
                
        print ("El máximo común divisor es: {}".format(res))  
    else: 
        for i in range (1,n):
            if n % i == 0 and m % i == 0:
                res = i
        print ("El máximo común divisor es: {}".format(res)) 
elif n % 2 != 0 and m % 2 != 0:
    #Si ambos valores son impares
    if n < m :
            for i in range (1,m):
                if n % i == 0 and m % i == 0:
                    res = i
            print ("El máximo común divisor es: {}".format(res))  
    else: 
        for i in range (1,n):
            if n % i == 0 and m % i == 0:
                res = i
        print ("El máximo común divisor es: {}".format(res)) 
else:    
    #si un valor es par y el otro impar
    if n > m:
        maxx = n
        
    else:
        maxx = m
        
    for i in range(n*m,maxx,-1):
        if i % n == 0 and i % m == 0 :
            res = i
    print ("El mínimo común múltiplo es: {}".format(res)) 
   