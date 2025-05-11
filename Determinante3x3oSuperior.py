import numpy as np
import math as m

#Este algoritmo usa el método de Gauss para hallar la determinante, y sirve para cualquier matriz cuadrada de 3x3 en adelante

#Funcion para sacar el valor de la determinante
def Determinante(A):
    #Primero, se despeja de tal forma que la matriz quede con un triángulo inferior de ceros.
    for i in range(filas-1):
        for j in range(i+1, filas):
            
            filatemp = A[i,i]*A[j,:] - (A[j,i]*A[i,:]) 
            A[j,:] = filatemp
    
    den = 1 #Variable donde se guardará el total del denominador, es 1 para que el producto no se anule
    k = 0 #Variable para escalar una posición cada vez que el ciclo cumpla un período
    
    #Ciclo para hallar el denominador, multiplicando y elevando a cierto número respectivamente
    for i in range(filas-2,0,-1):        
        den *= A[k,k]**i
        k += 1
        print(f"denominador = {den}")
    
    #Se divide el máximo valor de la matriz, en caso de ser una 3x3: A[3,3]; 4x4: A[4,4]; etc.
    det = A[filas-1,filas-1] / den    
                     
    return det
    
filas = 6   
matriz = np.array(  [
    [4, 1, 0, 2, 1, 3],
    [3, 2, 1, 0, 4, 5],
    [1, 0, 3, 2, 1, 0],
    [2, 1, 4, 3, 2, 1],
    [0, 1, 2, 1, 0, 3],
    [1, 2, 3, 4, 5, 6]
]
)

print(Determinante(matriz))