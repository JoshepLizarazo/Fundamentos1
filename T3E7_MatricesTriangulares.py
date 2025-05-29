import numpy as np

matriz = np.array([[1, 2, 3], [4,5,6], [7,8,9]])

forma = np.shape(matriz)    

if forma != (forma[0], forma[0]):
    print("La matriz introducida no es cuadrada")
    
else:
    if (matriz[1,0] or matriz[1,forma[0]-1]) != 0:
        print("No es una matriz triangular")
     
    elif matriz[0, :]:
         
        for i in range(1,forma[0]):
            
            for j in range(0, i):
                if matriz[i,j] != 0:
                    print("No es una matriz triangular")
                    exit()
                    