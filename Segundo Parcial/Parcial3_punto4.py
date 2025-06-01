import numpy as np

#Función para tomar los valores de tres en tres
def tresentres (A):
    tre = [] #Lista donde se depositarán los valores
    for i in range(0,len(A),3): 
        tre.append(A[i]) #Se introduce en la lista nueva el valor de la lista A en la posición i
    return tre

#Lista principal
lista = []

while True:
    n = input("Introduzca el número de elementos que desea que tenga la lista: ")
    
    try:
        n = int(n)
        break
    except:
        print("Error: Introduzca un número entero")

#Ciclo para introducir números aleatorios según n
for i in range(n):
    lista.append(np.random.randint(0,100)) #Introduce un valor aleatorio entre 0 y 99 a la lista

print(f"La lista es: {lista}")   
print(f"La lista tomando valores de tres en tres de la lista original es: {tresentres(lista)}")   
        