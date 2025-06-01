import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

while True:
    
    
    sel = input("Seleccione la opción que desea graficar: \n1. Graficar cantidad de ordenaciones \n2. Graficar cantidad de tiempo \n ")
    
    if int(sel) == 1:
        break
    elif int(sel) == 2:
        break
    else:
        print ("Error: Seleccione una opción válida")
        
        
def bubble_sort(L):
    ops = 0
    n = len(L)
    for i in range(n - 1):
        ops += 1 
        for j in range(n - i - 1):
            #operaciones += 1
            ops += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                ops += 1
                #intercambios += 1
        #print(f"paso {i + 1}: {L}")

    return L, ops

def insertion_sort(L):
    ops = 0
    i = 1
    while i < len(L):
        ops += 1
        j = i
        while j > 0 and L[j - 1] > L[j]:
            ops += 1
            #operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
            #intercambios += 1
            ops += 1
            j -= 1
        i += 1

    return L, ops   

def selection_sort(L):
    ops = 0
    lent = len(L)
    for i in range(lent - 1):
        ops += 1
        minn = i
        for j in range(i + 1, lent):
            ops += 1
            #operaciones += 1
            if (L[minn] > L[j]):
                ops += 1
                minn = j
        if minn != i:
            L[minn], L[i] = L[i], L[minn]
            ops += 1
            #intercambios += 1
            #operaciones += 1


    return L, ops

num_elements = np.arange(10, 101, 10)
print(num_elements)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)

o_bubble = np.zeros(size)
o_selection = np.zeros(size)
o_insertion = np.zeros(size)





for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16) # se crea el vector a ordenar    
    # acá se hace una copia de ese vector, para preservar el vector con números aleatorios.

    vector_ord = vector.copy()
    # acá viene la estructura para tomar el tiempo
    t_inicio = perf_counter_ns()
    A, ops= bubble_sort(vector_ord) # se ejecuta el método burbuja con el vector copia
    t_final = perf_counter_ns()
    o_bubble[i] = ops
    t_bubble[i] = t_final - t_inicio # se guarda el tiempo para n elementos, para crear una gráfica.
    print(f"Vector ordenado: \n{A}")
    vector_ord = vector.copy() # volvemos a copiar el vector aleatorio original sobre el vector copia para
    # que el siguiente método trabaje sobre los mismos datos
    print(f"Vector sin ordenar: \n{vector_ord}")
    t_inicio = perf_counter_ns()
    A, ops = insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    o_insertion[i] = ops
    t_insertion[i] = t_final - t_inicio
    #Insertion
    vector_ord = vector.copy()
    t_inicio = perf_counter_ns()
    A, ops = selection_sort(vector_ord)
    t_final = perf_counter_ns()
    o_selection[i] = ops
    t_selection[i] = t_final - t_inicio
    print(A)
    

if int(sel) == 2:
    plt.plot(num_elements, t_bubble, "g-", num_elements, t_insertion, "b-", num_elements, t_selection, "y-")
else:
    plt.plot(num_elements, o_bubble, "g-", num_elements, o_insertion, "b-", num_elements, o_selection, "y-")
plt.show()