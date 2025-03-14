'''La función de este programa es desplegar los valores menores que n hasta el mismo n, y detecta si cada uno de estos
valores es divisible por 2, 3 o 5, o todos, o un conjunto par de estos'''

print (" ")
n = int(input("Introduzca Número entero: "))

for i in range (1,n+1):
    A = i % 2 
    B = i % 3
    C = i % 5
    
    if A+B+C == 0:
        print("{}. es divisible por 2, 3 y 5".format(i))
    elif A == 0:
        if B == 0:
            print("{}. es divisible por 2 y 3".format(i))
        elif C == 0:
            print("{}. es divisible por 2 y 5".format(i))
        else:
            print("{}. es divisible por 2".format(i))
    elif B == 0:
        if C == 0:
            print("{}. es divisible por 3 y 5".format(i))
        else:
           print("{}. es divisible por 3".format(i)) 
    elif C == 0:
        print("{}. es divisible por 5".format(i))
    else :
        print (str(i) + ".")
            