'''
Algoritmo que saca el Seno aproximado de un ángulo en grados por medio de la serie de Taylor
'''

angulo = int(input("Introduzca el ángulo para sacar el seno: "))
x = (angulo * 3.14159) / 180 #Convertir el ángulo a radianes
n = int(input("Introduzca el rango de cifras significativas: "))
suma = 0 #valor total
for i in range (0, n+1):
    fact = 1
    kmax = 2 * i + 1 
    for k in range (1,kmax+1):
        fact = fact * k #Ecuación del denominador 
    suma = suma + (((-1)**i )*(x**(2*i+1)))/fact #Ecuación del numerador sobre fact 
print("El seno de " + str (angulo) + " grados es: " + str(suma))
