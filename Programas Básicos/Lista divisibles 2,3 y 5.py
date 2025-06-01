'''
Programa que imprime una lista de números que sean divisibles por 2, 3 y 5
'''

n = int(input("Cantidad de números: "))

for i in range(2, n+1):
    if i % 2 == 0: 
        print (i)
    elif i % 3 == 0:
        print (i)
    elif i % 5 == 0:
        print (i)
    