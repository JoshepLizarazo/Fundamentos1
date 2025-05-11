#Código hecho por Joshep Jared Lizarazo Montero
"""
El objetivo de este algoritmo es resolver un sistema de ecuaciones lineales 3x3, para esto, se usa el método de Gauss Jordan con
matrices, con el objetivo de que, el resultado final de la matriz quede de esta forma:

    [ 1 0 0  | a ]
    [ 0 1 0  | b ]
    [ 0 0 1  | c ]
    
Siendo a, b y c, los respectivos resultados para x1, x2 y x3  

"""
#Función para imprimir la matriz según como se encuentre en el momento
def matriz (a, b, c):
    print(f"\nEstado de la Matriz:\n[ {a[0]} {a[1]} {a[2]}  | {a[3]} ]")
    print(f"[ {b[0]} {b[1]} {b[2]}  | {b[3]} ]")
    print(f"[ {c[0]} {c[1]} {c[2]}  | {c[3]} ]\n")



#Las tres listas simulan cada fila de la matriz, para más facilidad 


A = [3, 2, 1, 39]
B = [4, 0, -1, 34]
C = [1, -2, 5, 26]


matriz(A, B, C)

    
#Función para convertir en cero el valor deseado en una fila
def ceros (a, b, c):  #a = Lista a cambiar,  b = Lista con la que se opera,  c = posición del valor a cambiar
    
    g = [] #Lista donde se insertan los resultados
    q = mulfil(a, b[c])
    p = mulfil(b, a[c])
    
    #print(q)
    
    if a[c] == 0:
        a = a
    else:
        #Si ambos valores tienen el mismo signo, se restan
        if (int(p[c]) < 0 and int(q[c]) < 0) or (int(p[c]) > 0 and int(q[c]) > 0):
            for i in range(len(a)):
                g.insert(i, int((p[i]) - q[i]))
                
            #a == b - mulfil(a, b[c])
            
        #En el caso contrario, se suman
        else:
            for i in range(len(a)):
                g.insert(i, int((p[i]) + q[i]))
            #a == b + mulfil(a, b[c]) 
    #print(g)
    return g
            

#Función para multiplicar una fila por cierto valor determinado 
def mulfil (a, b): #a = Fila a multiplicar,  b = Constante por la cual se multiplica
    
    c = [] #lista convertida, en la cual se depositarán los resultados
    
    for i in range(len(a)):
        c.insert(i, int(a[i])*b) #Multiplica cada valor de la lista y lo inserta en "c"
    return c

  


'''
Variación de la primera función con el mismo nombre, esta se emplea para el resultado final, y convierte en fracción el valor de "b"
en dado caso que la división final con este no dé un valor entero
'''
def mulfil2 (a, b): #a = Fila a dividir,  b = Posición del x
    
    w = a[3]/a[b] 
    c = a 
    q = mcd(int(a[3]), a[b]) #Saca el máximo común divisor entre b y el valor de x
    
    if w - int(w) == 0: #Si b dividido entre la "x" da entero, se hace esta operación y se deja el valor como está
        a.insert(4, int((a[3])/a[b]))
        a.pop(3)
    
    else: #En caso contrario, se dividen los valores de b y x por el mcd de ambos, para que el resultado sea una fracción simplificada
        y = [a[3], c[b]]
        
        #Detecta si ambos valores son negativos o el denominador es negativo para cambiar los signos
        if (y[0] < 0 and y[1] < 0) or (y[0] > 0 and y[1] < 0): 
            y.insert(1, y[0]*-1) 
            y.pop(0)
            y.insert(2, y[1]*-1) 
            y.pop(1)

        a.insert(4, f"{int(y[0]/q)} / {int(y[1]/q)}") #Se añaden los valores ya simplificados a la lista
        a.pop(3)
        
    
    a.insert(b+1, int((a[b])/a[b])) #Convierte el valor de x en 1 dividiéndolo por sí mismo
    a.pop(b)
    
    
    return a
    
    
#Función para sacar el Máximo común divisor, el cual será útil para ciertos casos
def mcd  (n, m):
    res = 0
    k = n
    r = m
    
    if k < 0:
        k = k*-1
    
    if r < 0:
        r = r*-1
    
                 
    if k < r :
        for i in range (1,r):
            if k % i == 0 and r % i == 0:
                res = i
                
        #print ("El máximo común divisor es: {}".format(res))  
        
    else: 
        for i in range (1,k):
            if k % i == 0 and r % i == 0:
                res = i
        #print ("El máximo común divisor es: {}".format(res)) 
        
    return res


"""
El primer paso es convertir el "x1" de la segunda y tercera fila en 0

Para esto, multiplicamos aquellas filas por el x1 de la primera fila, y los sumamos o restamos dependiendo el caso
esto es:
    
    [ x1 x2 x3   | b ]
    [ 0  x2 x3   | b ]
    [ 0  x2 x3   | b ]
    
"""

#Para la segunda fila (fila R2)
print(f"\nR2--> {B[0]}R1 ± {A[0]}R2\n")
B = ceros(B, A, 0)
matriz (A,B,C)

#Para la tercera fila 

#Para la segunda fila (fila R2)
print(f"\nR3--> {C[0]}R1 ± {A[0]}R3\n")
C = ceros(C, A, 0)
matriz (A,B,C)

"""
Ahora, convertimos el "x2" de la fila 3 (R3) en 0, multiplicando R3 por el "x2" de la segunda fila y sumando o restando,
dependiendo el caso, para que la matriz vaya quedando de esta forma:

    [ x1 x2 x3   | b ]
    [ 0  x2 x3   | b ]
    [ 0  0  x3   | b ]
    
"""

print(f"\nR3--> {C[1]}R2 ± {B[1]}R3\n")
C = ceros(C, B, 1)
matriz (A,B,C)

"""
El siguiente paso es convertir los "x3" de la primera y segunda fila (R1 y R2) en 0, para esto, multiplicaremos y haremos la respectiva operación
pero con el "x3"de la tercera fila (R3). El resultado se vería así:

    [ x1 x2 0    | b ]
    [ 0  x2 0    | b ]
    [ 0  0  x3   | b ]

"""

print(f"\nR1--> {A[2]}R3 ± {C[2]}R1\n")
A = ceros(A, C, 2)
matriz (A,B,C)

print(f"\nR3--> {B[2]}R3 ± {C[2]}R2\n")
B = ceros(B, C, 2)
matriz (A,B,C)

"""
Como uno de los últimos pasos, simplemente queda convertir "x2" de la primera fila (R1) en cero, para esto simplemenmte ejecutamos el
mismo procedimiento que las veces anteriores, multiplicando la fila entera por el valor de "x2" de la segunda fila (R2) y operamos
quedando de esta forma:

    [ x1 0  0    | b ]
    [ 0  x2 0    | b ]
    [ 0  0  x3   | b ]

"""

print(f"\nR3--> {A[1]}R2 ± {B[1]}R1\n")
A = ceros(A, B, 1)
matriz (A,B,C)

    
"""
Como último paso, dividiremos las equis restantes de cada fila por sí mismas para que el resultado sea uno, y si el número es negativo,
se divide por el mismo valor negativo para que el resultado sea positivo.

"""

print(f"\nR1--> R1/{A[0]}\n")
print(f"\nR2--> R2/{B[1]}\n")
print(f"\nR3--> R3/{C[2]}\n")



A = mulfil2(A, 0)
B = mulfil2(B, 1)
C = mulfil2(C, 2)


matriz (A,B,C)


print(f"Resultados representados en fracción:\nX1 = {A[3]}\nX2 = {B[3]}\nX1 = {C[3]}\n")
