
#Función para convertir la primera letra de cada palabra en mayúscula
def PrimeraMayus (A):
    lista = A.split(" ") #Convierte la cadena en lista para trabajarla de mejor forma
    k = [] #Lista en la cual se guardará la frase convertida
    
    #Ciclo para convertir la inicial de cada palabra en mayúscula
    for i in lista:
        k.append(i[0].upper() + i[1:])#Se añade a la lista K la palabra convertida. Se convierte en mayúscula la primera letra, se añade, y luego se añade el resto de la cadena  
    cadfin = " ".join(k) #Se convierte nuevamente en cadena toda la frase, con un espacio de separador
    return cadfin #Se la cadena convertida

#Introducir la palabra a convertir
a = str(input("Introduzca la palabra a convertir en mayúsculas sus iniciales: "))


print(PrimeraMayus(a))
    
        