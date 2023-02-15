
""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control: """
grArtemis = []
i=0
cant=int(len(grArtemis))
menu='1.'

while menu != '0':
    menu=(input("""
        --------------------El Menu-------------------
        1.   CREAR GRUPO ARTEMIS:
        1.1  LISTAR CAMPERS  DE ARTEMIS:
        1.2  AGREGAR CAMPERS A ARTEMIS:
        1.3  ELIMINAR CAMPERS DE ARTEMIS:
        1.4  ORDENAR ALFABETICAMENTE EN LA LISTA DE ARTEMIS:
        1.5  BUSCAR CAMPERS EN LA LISTA DE ARTEMIS:
        2.   CREAR GRUPO SPUTNIK:
        2.1  LISTAR CAMPERS DE SPUTNIK
        2.2  AGREGAR CAMPERS A SPUTNIK
        2.3  ELIMINAR CAMPERS DE SPUTNIK
        2.4  ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK
        2.5  BUSCAR CAMPERS EN LA LISTA DE SPUTNIK
        0:   PARA CERRER EL MENU
        ACCION QUE DESEA REALIZAR: """))
    if menu=='1.' or menu== '1':
        grArtemis = []
        print(f"\n\tSe ha creado el grupo Artemis")
    elif menu == '1.1' or  menu=='11':
        print("\n\tLos actuales campers de Artemis son")
        for i in range(cant):
            print(f'{i+1}. {grArtemis[i]}')
    elif menu == '1.2' or  menu=='12':
        cant=int(input("\n\tingrese la cantidad de integrantes que desea añadir: "))
        for i in range(cant):
            nom=(input(f'\n\tIngrese el nombre del nuevo campers para el grupo Artemis: ')).upper()
            grArtemis.append(nom)
        print(f"\n\tAgregado(s) exitosamente")    
    elif menu == '1.3' or  menu=='13':
        nom=input("\n\tIngrese el nombre del estudiante que sea eliminar : ").upper()
        grArtemis.remove(nom)
        print(f'\n\tEl estudiante {nom} fue eliminado del grupo Artemis')
    elif menu == '1.4' or  menu=='14':
        print("\n\tSe ordenan alfabeticamente la lista de Artemis")
        grArtemis.sort()
        for i in range(cant):
            print(f'{i+1}. {grArtemis[i]}')
    elif menu == '1.5' or  menu=='15':
        form=input('\n\tDigite 1 para buscar por numbre y digite 2 para buscar por numero: ')
        if form == '1':
            nom=input(f'\n\tcual es el nombre del campers: ').upper()
            pos=int((grArtemis.index(nom)))
            print(f'\n\t{pos+1}. {grArtemis[pos]}')
        elif form =='2':
            nom=int(input(f'\n\tEn que pocicion se encuentra? : '))
            print(f'{grArtemis[nom-1]}')
        else:
            print('debe insertar una opcion valida')
    elif menu == '2' or menu=='2.':
        grSpuknit = []
        print(f"\n\tSe ha creado el grupo Spuknit")
    elif menu == '2.1' or menu=='21':
        print("\n\tLos actuales campers de Spuknit son:")
        for i in range(cant):
            nom=(input(f'\n\tIngrese el nombre del nuevo campers para el grupo Spuknit: ')).upper()
            grSpuknit.append(nom)
    elif menu == '2.2' or menu=='22':
        cant=int(input("\n\tingrese la cantidad de integrantes que desea añadir: "))
        for i in range(cant):
            nom=(input(f'\n\tIngrese el nombre del nuevo campers para el grupo Spuknit  : ')).upper()
            grSpuknit.append(nom)
        print(f"\n\tAgregado(s) exitosamente")
    elif menu == '2.3' or menu=='23':
        nom=input("\n\tIngrese el nombre del estudiante que sea eliminar: ").upper()
        grSpuknit.remove(nom)
        print(f'\n\tEl estudiante {nom} fue eliminado de Spuknut')
    elif menu == '2.4' or menu=='24':
        print("\n\tSe ordenan alfabeticamente la lista de Spuknit")
        grSpuknit.sort()
        for i in range(cant):
            print(f'{i+1}. {grSpuknit[i]}')
    elif menu == '2.5' or menu=='25':
        form=input('\n\tDigite 1 para buscar por numbre y digite 2 para buscar por numero: ')
        if form == '1':
            nom=input(f'\n\tcual es el nombre del campers: ').upper()
            pos=int((grSpuknit.index(nom)))
            print(f'\n\t{pos+1}. {grSpuknit[pos]}')
    else:
        print("\n\tpor favor dijite una opcion valida")

    
































