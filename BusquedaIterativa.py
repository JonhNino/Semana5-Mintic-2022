#Programa para la busqueda binaria iterativa
# Jonh Niño
# hoy

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Funciones
def busqueda_binaria(lista,info_buscar):
    izq=0
    der=len(lista)-1
    while izq<=der:
        med=(izq+der)//2
        if info_buscar==lista[med]:
            return med
        elif info_buscar<lista[med]:
            der=med-1
        else:
            izq=med+1
    return -1
#Programa Principal
info_buscar=int(input("Informacion a buscar"))
resultado=busqueda_binaria(lista, info_buscar)#y Puedo utilzar resultado en vez de llamar tood el metodo
if busqueda_binaria(lista, info_buscar)==-1:
    print("La informacion",info_buscar,"NO se encuentra en la lista")
else:
    print("la Informacion",info_buscar,"Se encuentra en la posicion ", busqueda_binaria(lista, info_buscar))