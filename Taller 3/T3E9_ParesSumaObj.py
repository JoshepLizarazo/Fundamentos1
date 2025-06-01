'''
Este programa se encarga de buscar en una lista asignada por el usuario, pares de números en esta que, cuando son sumados,
den como resultado el número de suma objetivo, también asignado por el usuario
'''


n = int(input("Suma objetivo: "))
nums = []
suma = False

while True:
    m = input("\nIntroduce un número entero para introducir en la fila\no 0 para detener:  ")
    
    try:
        m = int(m)
        
        if m == 0:
            break
        else:
            nums.append(m)
            
    except:
        print("\nERROR: introduzca un número entero\n")
        
    
        
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if int(nums[i]) + int(nums[j]) == n:
            print(nums[i],nums[j])
            suma = True
    
if suma == False:
    print("\nNo hay ningún par en la lista que dé como resultado el número de suma objetivo\n")