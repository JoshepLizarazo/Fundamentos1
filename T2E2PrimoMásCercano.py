'''Este programa detecta el valor primo más cercano (menor o igual) de n'''


print("")
n = int(input("Introduzca un número mayor que 2: "))
if n <= 2:
    print ("Error: Introduzca un número mayor que 2")
d = 2
i = n
np = False 
fin = False 
while fin == False:
    if fin == False:
        np = False
        d = 2
        while np == False:
                if i % d == 0:
                    np = True
                    i = i-1
                elif d == i-1:
                    np = True
                    fin = True     
                else:
                    d = d + 1
    
print("El primo más cercano es: " + str(i))
print("")           




