'''Este programa es un menú que nos ofrece dos opciones simples, reconocer si el valor de n es par o impar, o reconocer si el valor de n es primo o no, y se sigue
ejecutando hasta que se le indique que pare'''

ter = False #Variable establecida para que el programa se siga ejecutando mientras su valor sea 'False'

while ter == False:

    print("")

    print ("Menú de operaciones")
    print ("1. Determinar si n es par o impar")
    print ("2. Determinar si n es primo o no")
    print ("3. Terminar programa")

    print("")

    o = int(input("Introduzca la operación que desea realizar: "))
    print ("")
    pr = True  
    if o < 1 or o > 3 : #Si los valores son diferentes a las opciones ofrecidas, da error
        print ("ERROR: Introduzca una opción válida")
    elif o == 3: #Opción 3: Termina el programa cambiando el valor de ter para que se deje de ejecutar el ciclo
                print ("Programa terminado: 5 en el parcial")
                ter = True

    else : #En dado caso que el usuario escoja una opción válida
        n = int (input("Introduzca un número entero positivo a evaluar: "))
        if n < 0:
            print ("ERROR: Introduzca un número entero positivo") #Es condición que n sea un número entero positivo, por lo que lo corrige si es negativo 
        else: 
            if o == 1: #opción 1: Establecer si n es par o impar
                if n % 2 == 0 :
                    print("{} es par".format(n))
                else:
                    print("{} es impar".format(n))
            elif o == 2: #Opción 2: Establecer si n es primo o no
                for i in range (2, n):
                    if n % i == 0:
                        pr = False
                if pr == True :
                    print("")
                    print ("{} es primo".format(n))
                else:
                    print("")
                    print("{} no es primo".format(n))
            
