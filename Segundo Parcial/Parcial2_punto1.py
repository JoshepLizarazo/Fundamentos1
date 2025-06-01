import numpy as np
import random as rnd

#Funció que hará el proceso de  generar la matriz y sacar los respectivos promedios de las diagonales principal y secundaria
def MatrizGen (n):
    matrix = np.zeros((n,n)) #Genera una matriz nxn llena de ceros con el número de filas/columnas deseado 
    filas = np.shape(matrix)[0] #Saca el valor n de la matriz nxn
    diag1 = [] #Lista donde se depositará la primera diagonal
    diag2 = [] #Lista donde se depositará la segunda diagonal
    
    #Ciclos para introducir los valores aleatorios a la respectiva matriz
    for i in range(n):
        temp = [] #Lista temporal donde se depositará la fila con los valores aleatorios
        for j in range (n):
            temp.append(rnd.randint(0,100)) #Genera e introduce los valores aleatorios a la la columna i de la fila j en la lista temporal
        matrix[i,:] = temp #Reemplaza la lista temporal con la fila i de la matriz
    print(f"\nMatriz generada:{matrix}\n")

    #Ciclo para sacar las respectivas diagonales de la matriz e introducirla en las listas
    for i in range(filas):
        diag1.append(matrix[i,i])
        diag2.append(matrix[i,(filas-1)-i])
    print(f"\nLa diagonal principal es: {diag1}\nLa diagonal secundaria es: {diag2}\n")
 
    #La función 'mean' saca el promedio de una respectiva lista, de esta manera tenemos como resultado los promedios de la primera y segunda diagonal  
    print(f"\nEl promedio de la diagonal principal es: {np.mean(diag1)}\n\nEl promedio de la diagonal secundaria es: {np.mean(diag2)}\n")
        
        
#Introducir el número de filas y columnas que se desea que tenga la matriz
num = int(input("Introduzca número de filas y columnas para la matriz: ")) 

#Llama a la función MatrizGen con 'num' como el condicional 
MatrizGen(num)