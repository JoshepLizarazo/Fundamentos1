

print("")
n = str(input("Introduzca la palabra a codificar: "))
A = list(n) #Se convierte la palabra a codificar en una lista
fradec = "" #Variable para introducir la palabra codificada

def deco (m, n):
    p = str(m)
    #print(ord(p))
    F = ""
    
    if (120 <= ord(p) <= 122 or 88 <= ord(p) <= 90) or ((ord(p) == 119 or ord(p) == 87) and n == 0):
        if n == 0: #Si la posición es par
            F = chr(ord(p)-23)  
            #print(f"Aquí está F1 holaaa {F}")
            return (F)
            
        
        else: #Si la posición es impar
            
            F = chr(ord(p)-22)
            #print(f"Aquí está F2 holaaa {F}")
            return (F)
    
    elif 64 < ord(p) <= 87 or 96 < ord(p) <= 119: #119 = w  87 = W
    
        if n == 0: #Si la posición es par
            F = chr(ord(p)+3)  
            #print(f"Aquí está F1 holaaa {F}")
            return (F)
            
        
        else: #Si la posición es impar
            
            F = chr(ord(p)+4)
            #print(f"Aquí está F2 holaaa {F}")
            return (F)
    else:
        F = m
        return(F)
    
    
    
for i in range(len(n)):
    pp = i % 2
    A.insert(i, deco(A.pop(i), pp))
    fradec += A[i]

#print(A)
print("")
print(f"{n} ----> {fradec}")