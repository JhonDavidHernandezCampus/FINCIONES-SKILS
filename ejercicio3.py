""" 3.  En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional.
El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """



def datos():
    nom=input("\tingrese el nombre del compretidor: ")
    slo=float(input(f"\tSueldo por kilometro recorrido para el competidor {nom}: "))  
    numKm=float(input(f"\tNumero de kilometros recorridos por el competidor {nom} durante toda la vuelta: "))
    numCaz=float(input(f"\tCuantos kilometros recorrio con la camizeta {nom} de lider: "))
    if numCaz > 1800:
        pagar=(slo*numKm)+(((numCaz-1800)*slo)*0.25)
        print(f'\t{nom} Resive el recargo del 25% y es de: {pagar}')
    if numKm >= 3277:
        pagar+=700000000
        print(f"\tEl competidor {nom} Gano la carrera se le paga en total: {pagar}")
    print(f'\tLo que se le debe pagar al competidor {nom} es de: {pagar}')
    return pagar

mas='SI'
while mas=='SI':
    datos()
    mas=input("\tDesea ingresar mas datos si o no?: ").upper()











