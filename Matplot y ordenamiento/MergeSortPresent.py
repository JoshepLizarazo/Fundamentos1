#Parte del código es cortesía de Chio Code

# O(nlogn)

A = []

while True:
    
    n = input("Introduzca un número entero o n para terminar de introducir valores: ")
    
    if n == "n":
        break
    else:
        try:
             num = int(n)
             A.append(int(n))
        except:
            print("\nERROR: Introuzca un número entero\n")

    print(A)


def mergeSort(arr):
    if len(arr) == 1:
        return arr


    mitad = len(arr) // 2
    izq_arr = arr[:mitad]
    der_arr = arr[mitad:]

    sorted_left_array = mergeSort(izq_arr)
    sorted_right_array = mergeSort(der_arr)

    return Merge(sorted_left_array, sorted_right_array)

def Merge(left_arr, right_arr):
    arr_res = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_res.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_res.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0:
        arr_res.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        arr_res.append(right_arr[0])
        right_arr.pop(0)

    return arr_res 

OrdA = mergeSort(A)
print(f"\nLista ordenada:\n{OrdA}")
