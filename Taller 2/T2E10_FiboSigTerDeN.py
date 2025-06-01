#Este programa despliega el valor siguiente de la sucesión de fibonacci que le sigue a n

print("")
n = int(input("Introduzca un valor: "))
print("")
val = 0
i = 1
cat = 0
reslin = ""
while i <= n:
    i = i + cat
    cat = val 
    val = i 
print("El siguiente valor de la serie de Fibonnacci es: {}".format(i))