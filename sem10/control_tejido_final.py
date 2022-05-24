import math

from config import (CTD_TENSORES, DESPERDICIO_ALAMBRE, DESPERDICIO_TEJIDO, PI,
                    ROTURAS_POSTES)


def verificar_formato_parcela():
	entrada = "N"
	while(entrada != "C" and entrada != "c" and entrada != "R" and entrada != "r"):
		print("________________")
		entrada = input("Formato de la parcela ([C]circular / [R]rectangular): ")
	
	return entrada.upper()

def calcular_perimetro(formato):
	perimetro = 0

	print("________________")
	if(formato == "C"):
		ingreso = input("Indicar radio parcela (mts): ")
		perimetro = 2 * PI * float(ingreso)
	else:
		largo = int(input("Indicar largo parcela (mts): "))
		ancho = int(input("Indicar ancho parcela (mts): "))
		perimetro = 2 * (largo + ancho)
	
	return perimetro

def solicitar_separacion_postes():
	print("________________")
	return int(input("Indicar separación entre postes (mts): "))

def calcular_tejido(per, sp):
	mts_tejido = math.ceil(per + (per * DESPERDICIO_TEJIDO / 100))
	mts_alambre = math.ceil(per * CTD_TENSORES + (per * DESPERDICIO_ALAMBRE / 100))
	ctd_postes_neta = math.ceil(per / sp)
	ctd_postes_real = math.ceil(ctd_postes_neta + (ctd_postes_neta * ROTURAS_POSTES / 100))
   
	calculos = { "tejido": mts_tejido, "alambre": mts_alambre, "postes": ctd_postes_real }
	
	return calculos


def main():
	formato = verificar_formato_parcela()
	perimetro = calcular_perimetro(formato)
	separacion_postes = solicitar_separacion_postes()
	datos = calcular_tejido(perimetro, separacion_postes)

	print(datos)


if (__name__ == "__main__"):
	main()
