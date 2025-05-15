import numpy as np

#Función que hará el proceso de sacar los valores en posiciones pares e impares. Sacará el promedio y sumatoria. Y Creará la lista nueva con las operaciones respectivas
def prom (A):
    print(f"\nLa lista es: {A}\n")
    
    #Se crea una lista B en la que se introducen los valores de A, menos el mínimo. En dado caso de que el valor mínimo sea 0
    B = []
    for j in range(len(A)):
        B.append(A[j])   
    B.remove(min(B))
    bmin = min(B)    
    
    par = [] #Lista donde se guardarán los valores pares
    impar = [] #Lista donde se guardarán los valores impares
    divparimpar = [] #Lista donde se guardarán las operaciones de los mínimos y máximos
    
    #Ciclo para introducir números de posiciones pares e impares en su respectiva lista
    for i in range(0,len(A),+2):
        par.append(A[i])
        if i+1 <= (len(A)-1):
            impar.append(A[i+1])
    print(par, impar)
    
    print(f"\nEl promedio de los elementos en posiciones pares es: {np.mean(par)}\nLa suma de los elementos en posiciones impares es: {sum(par)}")
    
    print()
    
    #Ciclo para hacer las respectivas operaciones de Dividir posición par por el máximo o posición par por el mínimo
    for i in range(len(A)):
        print(i)
        if i % 2 == 0:
            print((f"\nIntroducir en la lista: {A[i]} / {max(A)} = {A[i] / max(A)}\n"))
            
            divparimpar.append(A[i]/max(A))
        else:
            if min(A) == 0:
                print(f"\nIntroducir en la lista: {A[i]} / {bmin} = {A[i] / bmin}\n")
                divparimpar.append(A[i]/(bmin))
                
                           
            else: 
                print(f"\nIntroducir en la lista: {A[i]} / {min(A)}\n")
                divparimpar.append(A[i]/min(A))
                
            
            
    
    print(f"La lista posición par entre máximo e impar entre mínimo {divparimpar}")

#Lista que ingresará el usuario
lista = []


while True:
    n = int(input("Introduzca 1 si desea una lista con números aleatorios o 0 si desea introducirlos de forma manual: "))
    
    #Si el usuario introduce un valor correcto, va al siguiente paso, de otro modo, tendrá que volver a introducir un valor
    if n == 1 or n == 0:
        break
    
    else:
        print("Error: Introduzca 1 o 0")

#En dado caso que se quiera una lista de longitud n con números aleatorios
if n == 1:
    while True:
        val = input("Introduzca el número de valores que desea en la lista: ")
        try:
            val = int(val)
            break
        except:
            print("Error: Introduzca un número entero")
    for i in range(val):
        lista.append(np.random.randint(0,100)) #Introduce un valor aleatorio entre 0 y 99 a la lista

#Por otro lado, si se desea una lista con valores introducidos manualmente
else: 
    #Ciclo para introducir los valores 
    while True:
        val = input("Introduzca un número entero para añadir a la lista o N para terminar el proceso: ")
        
        if val == "N" :
            break
        else:
            try:
                val = int(val)
                lista.append(val)
            except:
                 print("Error: Introduzca un número entero o N")

prom(lista) 
