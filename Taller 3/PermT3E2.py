#Posibles permutaciones de una cadena de caracteres 

from math import factorial 

p =  str(input("Introduzca la cadena a permutar: "))
cad = list(p)



for i in range(len(cad)):
    for l in range(i+1,len(cad)-1):
        if (len(cad)-1) < l:
            break
        else:
            if cad[i] == cad[l]:
                cad.pop(l)
                
def perm (ls):
    if len(ls) == 0:
        return []
    if len(ls) == 1:
        return [ls]
    
    res = []
    for i in range(len(ls)):
        elem_act = ls[i]
        resto = ls[:i] + ls[i+1:]
    
        for k in perm(resto):
            res.append ([elem_act]+k)
            print(res)
        
    return res

perms = perm(cad)

for p in perms:
    print(''.join(p))

            
    
