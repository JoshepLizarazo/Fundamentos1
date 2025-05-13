import numpy as np

def transpuesta(A):
    
    trans = []

    for i in range(cols):
        t = []
        for j in range (filas):
           t.append(A[j,i])
        trans.append(t)
    
    rtrans = np.array(trans)

    return rtrans

matriz = np.array(
    [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
    ]
)

filas, cols = np.shape(matriz)

print(filas,cols)


print(matriz)

print(f"\nLa inversa es:\n{transpuesta(matriz)}")
