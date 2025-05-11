import numpy as np
import math as m

def MatrizInversa(A):
    #Crea una lista vacía para depositar la matriz inversa
    inv = []
    #Proceso para crear la matriz inversa según el número de filas que tenga la matriz 
    for k in range(filas):
        c = []
        for n in range(filas):
            c.append(1. if k == n else 0.)
        inv.append(c)
    v = np.array(inv)
    print(v)
                
    # proceso para fijar la fila de referencia y hallar el factor que anula el elemento correspondiente en la fila que se quiere reducir
    for i in range(filas):
        # i representa la fila que está siendo fijada
        for j in range(filas):
            # j representa la fila a comparar
            if i != j :
                print(f"Fila fija = {i}")
                print(v[j, :])
                if A[j, i] != 0:
                    factor = (-1) * (A[i, i] / A[j, i])
                    # multiplicar fila completa en j por factor y sumar fila en i
                    filatemp1 = A[i, :] + (factor) * A[j, :]
                    filatemp2 = v[i, :] + (factor) * v[j, :]
                    
                    print(filatemp2)
                    A[j, :] = filatemp1
                    v[j, :] = filatemp2
        print(f"Cambios después de fijar la fila {i}")
        print(v)
        
    # divir la fila completa de referencia por el valor en la diagonal para convertir en 1 para A, y dar el resultado para v
    for i in range(filas):
        v[i, :] /= (A[i, i])
        A[i, :] /= (A[i, i])
        
    
    return v
    #fin del def de gauss jordan

""" filas = int(input("introduzca el número de filas, o de ecuaciones: "))
cols = int(input("introduzca el número de columnas, o de "equis":

matriz = np.zeros((filas, cols))

for i in range(filas):
    for j in range(cols):
        matriz[i, j] = float(input(f"Introduzca el elemento para la posición {i + 1}, {j + 1} de la matriz: "))

print("La matriz es:")
print(matriz) """

filas = 3
cols = filas 
matriz = np.array([[ 3.,  5.,  0.],  [ 3.,  6.,  2.],  [ 3.,  2.,  1.]])

print(matriz)

# invocar la función Matriz Inversa
matriz_i = MatrizInversa(matriz)

print(matriz_i)

    
            
                