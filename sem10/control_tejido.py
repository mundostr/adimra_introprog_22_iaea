import math

DESPERDICIO_TEJIDO = 2 # %
DESPERDICIO_ALAMBRE = 2 # %
ROTURAS_POSTES = 1 # %
CTD_TENSORES = 3 # unidades
PI = 3.1415926


formato_parcela = ""


def verificar_formato_parcela():
    entrada = "N"
    while(entrada != "C" and entrada != "c" and entrada != "R" and entrada != "r"):
        entrada = input("Formato de la parcela ([C]circular / [R]rectangular): ")
    
    return entrada.upper()


def calcular_perimetro(formato):
    perimetro = 0

    if(formato == "C"):
        ingreso = input("Indicar radio parcela (mts): ")
        perimetro = 2 * PI * float(ingreso)
    else:
        largo = int(input("Indicar largo parcela (mts): "))
        ancho = int(input("Indicar ancho parcela (mts): "))
        perimetro = 2 * (largo + ancho)
    
    return perimetro


def solicitar_separacion_postes():
    return int(input("Indicar separacion entre postes (mts): "))


def calcular_tejido(per, sp):
    mtrs_tejido = math.ceil(per + (per * DESPERDICIO_TEJIDO / 100))
    mtrs_alambre = math.ceil(per * CTD_TENSORES + (per * DESPERDICIO_ALAMBRE / 100))
    cantidad_postes_neta = math.ceil(per / sp)
    cantidad_postes_real = math.ceil(cantidad_postes_neta + (cantidad_postes_neta * ROTURAS_POSTES / 100))
   
    calculos = { "tejido": mtrs_tejido, "alambre": mtrs_alambre, "postes": cantidad_postes_real }
    
    return calculos


def main():
    formato_parcela = verificar_formato_parcela()
    perimetro = calcular_perimetro(formato_parcela)
    separacion_postes = solicitar_separacion_postes()
    print(calcular_tejido(perimetro, separacion_postes))


def main2():
    global entrada, formato_parcela
    
    perimetro = 0 # variable local

    while(entrada != "C" and entrada != "c" and entrada != "R" and entrada != "r"):
        entrada = input("Formato de la parcela ([C]circular / [R]rectangular): ")
    
    formato_parcela = entrada.upper()

    if(formato_parcela == "C"):
        ingreso = input("Indicar radio parcela (mts): ")
        perimetro = 2 * PI * float(ingreso)
    else:
        largo = int(input("Indicar largo parcela (mts): "))
        ancho = int(input("Indicar ancho parcela (mts): "))
        perimetro = 2 * (largo + ancho)
    
    separacion_postes = int(input("Indicar separacion entre postes (mts): "))
    
    mtrs_tejido = math.ceil(perimetro + (perimetro * DESPERDICIO_TEJIDO / 100))
    mtrs_alambre = math.ceil(perimetro * CTD_TENSORES + (perimetro * DESPERDICIO_ALAMBRE / 100))
    cantidad_postes_neta = math.ceil(perimetro / separacion_postes)
    cantidad_postes_real = math.ceil(cantidad_postes_neta + (cantidad_postes_neta * ROTURAS_POSTES / 100))

    print(mtrs_tejido)
    print(mtrs_alambre)
    print(cantidad_postes_real)


if (__name__ == "__main__"):
    main()
