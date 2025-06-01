#Este programa despliega los valores de la sucesión de Fibonacci menores o iguales a n

print("")
n = int(input("introduzca un valor: "))
print("")
val = 0
i = 1
cat = 0
reslin = ""
while i <= n:
    i = i + cat
    cat = val 
    val = i 
    
    if cat == 0 :
        reslin = str(cat) 
     
    else:
        reslin = reslin + ", " + str(cat)
    
    print (cat)

print ("")
print("Sucesión: " + reslin) #Despliega los valores menores o iguales a n en fila  
