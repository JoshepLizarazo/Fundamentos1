import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
import random as rnd


def bubble_sort(L):
    
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return (L)

def selection_sort(L):
    n = len(L)
    for i in range(n - 1):
        minn = i
        for j in range(i + 1, n):
            if (L[minn] > L[j]):
                minn = j
            if minn != i:
                L[minn], L[i] = L[i], L[minn]
        return (L)


def insertion_sort(L):
        i = 1
        n = len(L)
        while i < n:
            j = i
            while j > 0 and L[j - 1] > L[j]:

                L[j], L[j - 1] = L[j - 1], L[j]
               
                j -= 1
            i += 1
            return (L)
    

num_elements = np.arange(100, 1001, 100)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    #Para Bubble
    t_inicio = perf_counter_ns()
    bubble_sort(vector_ord)
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio
    #Para Selection
    t_inicio = perf_counter_ns()
    selection_sort(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i] = t_final - t_inicio
    #Para Insertion
    t_inicio = perf_counter_ns()
    insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio
    
print(t_insertion)
print(t_selection)
print (t_bubble)
plt.plot(num_elements, t_bubble, "g-", num_elements, t_selection, "r-", num_elements, t_insertion, "y-")
plt.show()