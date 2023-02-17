import json
""" 4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general. """



datos=[]

can=int(input("cuantos almacenes son: "))
for i in range(can):
    print("\n -------------NUEVO ALMACEN--------------")
    nomAlma=input('Nombre del almacen: ')
    for i in range(5):
        tpArt=input(f'Tipo de articulo: ')
        canVen=int(input('Cantidad de unidades vendias: '))
        veDic={'nombre':nomAlma,'Tipo':tpArt,'Cantidad':canVen }
        print(veDic)
        datos.append(veDic)


print(json.dumps(datos,indent=4) )
for i in datos:
    print(i["Cantidad"])





