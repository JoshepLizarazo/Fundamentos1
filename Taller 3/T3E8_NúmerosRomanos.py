#Este programa convierte números naturales a caracteres romanos desde el 1 hasta 9999

import numpy as np

romans =  [['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], 
           ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], 
           ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
           ['', 'M', 'MM', 'MMM', 'MV¯','V¯','V¯M','V¯MM','V¯MMM','V¯X¯']]

romansarr =()

n = input("\nIntroduzca el valor a convertir en números romanos:  ")

res = ""

try:
    n = abs(int(n))
    num = str(n)
except: 
    print("ERROR: Introduzca un número entero")
    
    
for i in range(len(num)):

    res = romans[i][int(num[(len(num)-1)-i])] + res 


print(f"\n{n} convertido a números romanos es: {res}\n")
    