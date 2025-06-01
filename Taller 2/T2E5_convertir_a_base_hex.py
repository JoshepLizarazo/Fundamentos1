'''La función de este programa es convertir un número decimal a una base de 2, 4, 8 o 16 según la elección
del usuario'''

print (" ")
print("Conversión de número decimal a base X")
print (" ")
n = int(input("Introduzca el valor a convertir: "))
print (" ")
print("1. Convertir a base 2")
print("2. Convertir a base 4")
print("3. Convertir a base 8")
print("4. Convertir a base 16")
b = int(input("Introduzca la opción de valor a convertir (de 1 a 4): "))

if b < 1:
    print (" ")
    print ("ERROR: opción de base inválida")
elif b > 4:
    print (" ")
    print ("ERROR: opción de base inválida")
else:
    if b == 1:
        val = 2
    elif b == 2:
        val = 4
        
    elif b == 3:
        val = 8
        
    elif b == 4:
        val = 16
res = 0
hexres = ""
factor = 1 

    

if 1<=b<=4:
    if b == 4:
        while n > 0:
            
            r = n % val #Residuo de n dividido entre val
            if r > 9:
                if r == 10:
                    r = "A"
                elif r == 11:
                    r = "B"
                elif r == 12:
                    r = "C"
                elif r == 13:
                    r = "D"
                elif r == 14:
                    r = "E"
                elif r == 15:
                    r = "F"    
            else: 
                r = str(r)
            n = n // val #división entera, ignorando la parte decimal 
            hexres = r + hexres
            
        res = hexres
            
    else:
        while n > 0:
            
            r = n % val #Residuo de n dividido entre val
            n = n // val #división entera, ignorando la parte decimal 
            res = res + factor * r #Depositar el valor por cada paso 
            factor = factor * 10 #multiplicar el factor por 10 para que la cifra siguiente se deposite a la derecha
    print (" ")       
    print ("El resultado es: {}".format(res))
    print("")