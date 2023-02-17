
""" 4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general. """

lista=[]
matriz=[]
print(matriz)

def pedirArt():
    nomAlma=input('Nombre del almacen: ')
    for i in range(5):
        tpArt=input(f'Tipo de articulo: ')
        canVen=int(input('Cantidad de unidades vendias: '))
        lista.append(nomAlma)
        lista.append(tpArt) 
        lista.append(canVen)
        matriz.append(lista)
        print(f'{lista}')
        print(matriz)
        lista.clear()
        print(f'{lista}')
    return matriz

Can= int(input(f"Cuantos almacenes son: "))
i=0
while Can>i:
    i+=1
    pedirArt()
    print(matriz)
