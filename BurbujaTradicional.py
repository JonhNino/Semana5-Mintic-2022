#Programa ordenamiento metodo burbuja tradicional 
# JONH NIÑO 
# HOy

lista=[]
#Funciones para Programa 
def ordenamiento_burbuja(lista):
    for i in range(N-1):
        for j in range(i+1,N):
            if lista[i]>lista[j]:#Si quiero de manera descente <
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista

#Programa Principal
N=int(input("Cantidad Elementos: "))
for i in range(N):
    numero=int(input("Numero Entero: "))
    lista.append(numero)
#Imprimir lista sin ordenar
print("Lista Original")
for i in range(N):
    print(lista[i])

#Ordenar Lista
lista=ordenamiento_burbuja(lista)
#Imprimir Lista
print("Lista Ordenada")
for i in range(N):
    print(lista[i])

