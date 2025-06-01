salir = False

'''
Calculadora que ejecuta diversas operaciones según la necesidad del usuario
'''

while salir != True: 

    print ("Menu")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicación")
    print ("4. División")
    print ("5. Salir")
    n = int(input("Introduzca la operación que desea realizar: "))
    res = 0 

    if n == 5:
        salir =  True
    elif n > 5: 
        print ("ERROR: valor no válido (Escoja un número de 1 a 5)")
        print (" ")
    elif n < 1:
        print ("ERROR: Valor no válido (Escoja un número de 1 a 5)")
        print (" ")
    else: 
        n1 = int(input("Introduzca el primer número: "))
        n2 = int(input("Introduzca el segundo número: "))
        if n == 1:
            res = n1 + n2
            print ("{} + {} = {} ".format(n1, n2, res))
            print (" ")
        elif n == 2:
            res = n1 - n2
            print ("{} - {} = {} ".format(n1, n2, res))
            print (" ")
        elif n == 3:
            res = n1 * n2
            print ("{} * {} = {} ".format(n1, n2, res))
            print (" ")
        elif n == 4:
            if n2 == 0:
                print("ERROR: Valor no válido (No se puede dividir por 0)")
                print (" ")
            else:    
                res = n1 / n2
                print ("{} / {} = {} ".format(n1, n2, res))
                print (" ")
print ("Programa Terminado")
    
        
