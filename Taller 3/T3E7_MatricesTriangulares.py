import numpy as np

matriz = np.array(input())

#Espacio donde el usuario introducirá la matriz respectiva
forma = np.shape([[1, 0, 0], [0,1,0], [0,0,9]])    

formaprac = forma[0]-1 #Toma solamente el primer valor del tamaño de la matriz y lo resta por uno para fines prácticos

def triangs(A):
    
    if A[0,1] == 0 or A[2,2] == 0 :
        sup = False
        inf = False
        
        if A[1, 0] == 0: 
            for i in range(1,forma[0]):    
                for j in range(0, i):
                    if A[i,j] != 0:
                        break
                        
                    if i == formaprac and j == formaprac-1:
                        inf = True
                        
        if A[0,formaprac] == 0:
                for i in range(formaprac-1,-1,-1):    
                    for j in range(formaprac, 0+i, -1):
                        if A[i,j] != 0:
                            break

                        if i == 0 and j == 1:
                            sup = True
        
        if sup == True and inf == True:
            return "La matriz es triangular superior tanto como inferior"
        
        elif sup == True:
            return "La matriz es triangular superior"
        
        elif inf == True:
            return "La matriz es triangular inferior"
        
        else: 
            return "La matriz no es triangular superior ni inferior"

if forma != (forma[0], forma[0]):
    print("La matriz introducida no es cuadrada")                     

else:
    if matriz[0,1] == 0 or matriz[formaprac,formaprac-1] == 0 :
        print(triangs(matriz))