#Programa ordenamiento burbuja de varias listas (Ascendente) (N elemmentos)
#Autor: Jonh
# Fecha Hoy

#Funcion Ordenamiento
def ordenamiento_burbuja(lista_productos,lista_precios):
    for i in range(N-1):
        for j in range(i+1,N):
            if lista_productos[i]>lista_productos[j]:
                temp=lista_productos[i]
                lista_productos[i]=lista_productos[j]
                lista_productos[j]=temp
                temp1=lista_precios[i]
                lista_precios[i]=lista_precios[j]
                lista_precios[j]=temp1
    return lista_productos,lista_precios

#Programa Principal
lista_productos=[]
lista_precios=[]
N=int(input("Cantidad De Productos: "))
for i in range(N):
    producto=input("Producto: ")
    precio=float(input("Precio: "))
    lista_productos.append(producto)
    lista_precios.append(precio)
#Imprimir Listas
for i in range(N):
    print("Producto: ",lista_productos[i])
    print("Precio: ",lista_precios[i])
lista_productos,lista_precios=ordenamiento_burbuja(lista_productos, lista_precios)
#Imprimir Listas
for i in range(N):
    print("Producto: ",lista_productos[i])
    print("Precio: ",lista_precios[i])
