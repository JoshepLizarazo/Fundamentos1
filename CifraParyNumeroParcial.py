'''La Función de este programa es evaluar cada una de las cifras en el número introducido, e identificar si estas son pares o impares, finalmente,
nos dice qué número de cifras contiene dicho número'''

print("")

n = int(input("Introduzca un valor entero positivo: ")) 
p = str(n) #Convierte el valor de n a cadena para poder evaluar sus números como caracteres
t = len(p) #Nos da el valor numérico de las cifras que contiene n

print("")

if n < 0:
    print("ERROR: Introduzca un valor entero positivo")

else:
    for i in range (t): #Ciclo el cual va a evaluar las cifras una por una 
        if int(p[i]) % 2 == 0: #Si el residuo de la cifra en la posición i dividida entre 2 es igual a 0, se asume que es par
            print ("{} es par.".format(p[i])) #Se imprime la afirmación
        
        else: #De otro modo, entonces se puede asumir que el núero es impar
            print("{} es impar.".format(p[i]))

    print("")
    print("El número {} tiene {} cifras en total".format(n, t)) #Como ya se había expresado en un principio, t indica cuantas cifras contiene n, lo suamos para que nos demuestre esto
    print ("")