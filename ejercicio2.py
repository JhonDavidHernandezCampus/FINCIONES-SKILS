""" 2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """


nomAtletas=[]
marSalto=[]
i=1
salir='SI'
while salir=='SI':
    nom=input("digite el nombre del atleta: ")
    nomAtletas.append(nom)
    mar=float(input(f'Cual fue la medida del salto en metros de la persona {nom}: '))
    marSalto.append(mar)
    salir=input("Va a ingresar los datos de otro atleta si o no? \n").upper()
    
def  salMayor():
    can=len(marSalto)
    mayor=marSalto[0]
    for i in range(can):
        if mayor < marSalto[i]:
            mayor=marSalto[i]
    return  mayor


rec=float(15.50)
j=0
pos=marSalto.index(salMayor())
print(f'\tLa persona ganadora es {nomAtletas[pos]}\n\t Se lleva la medalla de ORO ')
if salMayor() > rec:
    print(f'\tY se lleva 500 millones por romper el record') 
else:
    print(f'\tLa competidora gano pero no supero el record')
