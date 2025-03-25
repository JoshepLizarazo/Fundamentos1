import matplotlib.pyplot as plt
import math as m
import random as rnd

X = []
Y = []
X1 = []
Y1 = []

n = 100
inc = 200

mm = 0
b = 0

sumx = 0
sumy = 0
sumxy = 0 
sumx2 = 0
antx = 0 
antxy = 0 



for i in range(n):
    X.append(rnd.randint(40, 201))
    sumx += X[i]

for i in range (n):
    Y.append(rnd.randint(150, 201))
    sumy += Y[i]

for i in range (n):
    sumxy = X[i]*Y[i] + antxy 
    antxy = sumxy

for i in range (n):
    sumx2 = X[i]**2 + antx
    antx = sumx2


mm = (n * antxy - sumx * sumy) / (n*antx-(sumx))**2

b = (sumy  * antxy - sumx * antxy) / (n * antx - (sumx)**2)

for i in range (n):
    Y1.append(mm*i+b)
    X1.append(i)

plt.plot(X1, Y1, "g-", X1, Y1, "r*")
plt.show()


