import random as rnd

media = 0
varianza = 0
deves = 0
rango = 0


A = []
print("")
print("1. Números aleatorios")
print("2. Introducir números manualmente")

n = int(input("Seleccione la opción: "))
print("")

if n < 1 or n > 2: 
    print("Error: introduzca una ocpión válida")

else:
        if n == 1: #función para cuando el usuario decida números aleatorios
            b = int(input("Introduzca la cantidad de valores aleatorios: "))
            for i in range(b):
                A.append(rnd.randint(0,100)) #Los números estarán en un rango de 0 a 99

        else: 

            while True: #Crea un bucle infinito 
                e = input("Introduzca un número entero a añadir, o N si desea terminar el conteo: ")
        
                if e.upper() == "N": #Convierte la entrada a mayúscula para que se ejecute aún así la n sea en minúscula 
                    print("Conteo terminado")
                    break #Rompe el ciclo, para que se deje de repetir
                
                if e.isdigit(): #Se establece para cuando e es un múmero entero
                    A.append(int(e))
                
                else:
                    print ("Entrada no válida: Introduzca un número entero o N si desea terminar el conteo")
        
        print("")
        print(A)
        print("")
        
        for i in A: 
            media += i #Hace que cada uno de los valores de la lista se sumen
        
        media /= len(A) #Divide la suma de los valores entre la cantidad de valores que hay en la lista
        
        print(f"La media es {media}")
            
            

        def vmmc(n): #Función que da la sumatoria de cada uno de los valores de la lista, restado por la media y elevado al cuadrado
            vmm = (n-media)**2
            return(vmm)
        
    
        
        for i in A: 
            varianza += vmmc(i)
        
       
        varianza = varianza / (len(A)) #Divide el resultado de el ciclo en la cantidad de valores (Formula de la varianza)
        deves = (varianza)**1/2
        
        rango = max(A) - min(A) #Resta el valor máximo con el mínimo para sacar el rango 
        
        print(f"La varianza es {varianza:.2f}") #Redondea el número de decimales para que solo sean dos en el resultado
       
        print(f"La desviación estandar es {deves:.2f}")
        
        print(f"El rango es: {rango}")
        
        
        
            
            
        
                    