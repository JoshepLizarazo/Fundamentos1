'''
El funcionamiento de este código es codificar o decodificar una frase con el cifrado de Cesar. A su vez, dependiendo de la posición de la palabra (si es par o 
impar), hace el desplazamiento de las letras 3 o 4 posiciones.
'''

qq = int(input("1. Codificar\n2. Decodificar\nEscoja la operación que desea realizar: "))

print("")
n = str(input("Introduzca la palabra a codificar: "))
A = list(n) #Se convierte la palabra a codificar en una lista
fradec = "" #Variable para introducir la palabra codificada (resultado final)



def deco (m, n): #Función que hará el procedimiento de convertir palabra por palabra

    print(n)
    p = m 
    F = "" #Variable donde irá la letra convertida 
    
    '''
    Al usarse los valores respectivos ASCII, se tiene que hacer una condicional aparte para las letras con los números mayores,
    ya que, si se le suma al valor ASCII de estos, el resultado será un caracter diferente a una letra. Ej: z = 122(valor ascii).  122 + 3 = 125.  125 (valor ascii) = "}" 
    '''
    
    #Condicional para dichas letras
    if (120 <= ord(p) <= 122 or 88 <= ord(p) <= 90) or ((ord(p) == 119 or ord(p) == 87) and n == 0):
    
        if n == 0: #Si la posición es par
            F = chr(ord(p)-22)  
                  
        else: #Si la posición es impar
            
            F = chr(ord(p)-21)               
        
    #Condicional para el resto de letras 
    elif 64 < ord(p) <= 87 or 96 < ord(p) <= 119: #119 = w  87 = W
    
        if n == 0: #Si la posición es par
            F = chr(ord(p)+3)             
        
        else: #Si la posición es impar
            
            F = chr(ord(p)+4)
    
    #Si la variable m no es una letra, entonces, no se reemplaza por nada
    else: 
        F = m
    
    return(F)

def desco (m, n):
    
    ''' 
    Esta función ejerce lo mismo que la anterior, pero al contrario.
    '''
    
    p = m 
    F = "" #Variable donde irá la letra convertida 
        
    #Condicional para dichas letras
    if (65 <= ord(p) <= 67 or 97 <= ord(p) <= 99) or ((ord(p) == 100 or ord(p) == 68) and n == 0):
    
        if n == 0: #Si la posición es par
            F = chr(ord(p)+22)  
                  
        else: #Si la posición es impar
            
            F = chr(ord(p)+21)               
        
    #Condicional para el resto de letras 
    elif 69 <= ord(p) <= 90 or 101 < ord(p) <= 122: #119 = w  87 = W
    
        if n == 0: #Si la posición es par
            F = chr(ord(p)-3)             
        
        else: #Si la posición es impar
            
            F = chr(ord(p)-4)
    
    #Si la variable m no es una letra, entonces, no se reemplaza por nada
    else: 
        F = m
    
    return(F)      
    
for i in range(len(n)):
    
    pp = 0 #Esta variable define si la posición de la palabra es par o impar. Empieza desde la posición '0', que es par
    re= 0 #Variable auxiliar que ayuda a cambiar el valor de pp
    
    if A[i] == " ": #En esta parte, se detecta si hay un espacio, lo cual significa que la siguiente palabra cambia de posición (Par o impar)
        re += 1
        pp = re % 2
        
    if qq == 1:
        A.insert(i, deco(A.pop(i), pp)) #Se llama a la función, y, a su vez se reemplaza el valor i de la lista, por el valor convertido por la función  
    
    elif qq == 2:
        A.insert(i, desco(A.pop(i), pp))
        
    fradec += A[i] #Se añade la letra convertida a la cadena que tendrá el resultado final

#print(A)
print("")
print(f"{n} ----> {fradec}")
print("")
