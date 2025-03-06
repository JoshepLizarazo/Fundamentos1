n = int(input("Introduzca el número a convertir: ")) 
b = int(input("Introduzca el número base a convertir: "))
resultado = 0 #Variable vacía para depositar el resultado final
factor = 1
r= 0 #factor que moverá las cifras
if b < 2:
    print ("base inválida")
elif b > 9:
    print ("base inválida")
else:
    while n > 0:
        
        r = n % b #Residuo de n dividido entre b 
        n = n // b #división entera, ignorando la parte decimal 
        resultado = resultado + factor * r #Depositar el valor por cada paso 
        factor = factor * 10 #multiplicar el factor por 10 para que la cifra siguiente se deposite a la derecha
        print (resultado) 
print (resultado)
