'''PENDIENTES:
1. Reemplazar antx y antxy por sus correspondientes
2. Modificar lista de X y Y principal
3. Comentar to'
4. Agregar prints de resultado
5. Descomentar cosas'''


import matplotlib.pyplot as plt
import math as m
import random as rnd

''' Ejemplo para comprobar 
X = [162, 127, 72, 191, 106, 112, 110, 79, 143, 63, 201, 151, 184, 48, 147, 88, 59, 138, 156, 156, 41, 144, 127, 62, 132, 43, 113, 121, 45, 86, 61, 171, 130, 124, 104, 116, 110, 54, 100, 162, 95, 196, 59, 156, 181, 50, 74, 151, 196, 103, 144, 100, 176, 113, 138, 112, 68, 116, 181, 87, 50, 94, 160, 159, 90, 167, 151, 182, 124, 106, 127, 125, 131, 167, 186, 120, 93, 198, 85, 139, 189, 56, 84, 155, 67, 81, 61, 152, 115, 85, 141, 85, 106, 63, 99, 104, 184, 102, 143, 54]
Y = [160, 172, 186, 196, 195, 157, 157, 172, 172, 191, 176, 200, 159, 185, 152, 175, 190, 160, 159, 150, 158, 153, 169, 184, 167, 154, 167, 189, 176, 165, 195, 197, 195, 157, 167, 174, 199, 193, 173, 155, 201, 185, 162, 189, 171, 155, 196, 173, 155, 191, 201, 177, 196, 190, 183, 150, 161, 181, 183, 173, 194, 178, 198, 194, 163, 160, 194, 158, 184, 155, 188, 183, 162, 163, 197, 151, 172, 154, 170, 159, 201, 152, 151, 157, 172, 183, 195, 182, 157, 153, 176, 151, 199, 162, 159, 177, 154, 171, 167, 157]
'''
X = []
Y = []
X1 = []
Y1 = []

n = 100 #Número de valores que serán generados en X y Y



mm = 0 #Pendiente
b = 0 #Valor independiente

sumx = 0 #Valor sumatoria de X
sumy = 0 #Valor sumatoria de Y
sumxy = 0 #Sumatoria de la multiplicación ente X y Y
sumx2 = 0 #Sumatoria de X al cuadrado
antx = 0 
antxy = 0 



for i in range(n):
    #X.append(rnd.randint(40, 201))
    sumx += X[i]

for i in range (n):
    #Y.append(rnd.randint(150, 201))
    sumy += Y[i]

for i in range (n):
    sumxy = X[i]*Y[i] + antxy 
    antxy = sumxy

for i in range (n):
    sumx2 = X[i]**2 + antx
    antx = sumx2

print(X)
print(Y)

mm = (n * antxy - sumx * sumy) / (n*antx-(sumx)**2)

b = (sumy  * antx - sumx * antxy) / (n * antx - (sumx)**2)

print(mm)
print(b)
print(f"Fo")

for i in range (n):
    Y1.append(mm*i+b)
    X1.append(i)

plt.plot(X1, Y1, "g-")
plt.show()


'''y = 0,0091x + 172,7 Resultado de la ecuación y=mx+b del ejemplo'''

