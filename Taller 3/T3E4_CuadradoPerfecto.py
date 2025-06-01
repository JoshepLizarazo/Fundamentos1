
import math
i = 0
n = int(input("Introduzca el número para encontrar su múltiplo que dé cuadrado perfecto: "))
if math.sqrt(n) == int(math.sqrt(n)):
    print("El mismo número introducido es un cuadrado perfecto")

else:
    while True:
        i += 1
        if math.sqrt(n*i) == int(math.sqrt(n*i)):
            print(f"El número a multiplicar con {n} para que dé una raiz cuadrada es {i}")
            break
    