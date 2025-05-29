import numpy as np

matriz = np.array([[1, 0, 0], [4,5,0], [7,8,9]])

forma = np.shape(matriz)    

if forma != (forma[0], forma[0]):
    print("La matriz introducida no es cuadrada")
    
else:
    if matriz[0,1] == 0 or matriz[2,2] == 0 :
        if matriz[1, 0] == 0: 
            for i in range(1,forma[0]):    
                for j in range(0, i):
                    if matriz[i,j] != 0:
                        print("No es una matriz triangular inferior")
                        break
                    if i == forma[0]-1:
                        print("Es una matriz triangular inferior ")
                        
        if matriz[0,forma[0]] == 0:
                for i in range(forma[0]-2,-1,-1):    
                    for j in range(forma[0]-1, 0, -1):
                        if matriz[i,j] != 0:
                            print("No es una matriz triangular superior")
                            break
                        if i == 0:
                            print("Es una matriz triangular superior")
                        
