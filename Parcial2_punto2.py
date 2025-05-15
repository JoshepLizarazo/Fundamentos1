import numpy as np

def prom (A):
    print(A)
    j = 1
    par = []
    impar = []
    for i in range(0,len(A),+2):
        par.append(A[i])
        impar.append(A[i+1])
    print(par, impar)


prom([1,2,3,4,5]) 