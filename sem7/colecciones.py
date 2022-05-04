"""
Término gral: matriz (array)

Listas -> corchetes
Tuplas -> paréntesis
Diccionarios -> llaves
"""


# Listas (mutable)
lista_lecturas = [23, 22, 21, 25, 15, 18, 1]
# for c1 in range(6):
# for lectura in lista_lecturas:
	# print(lectura)
	# print(lista_lecturas[c1])


# Tuplas (inmutable)
tupla_lecturas = (15, 12, 11, 15, 16)
# for c1 in range(5):
# for lectura in tupla_lecturas:
	# print(tupla_lecturas[c1])


DIAS_SEMANA = ( "Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom" )


# Diccionarios
datos_personales = {
	"nya": "Carlos Perren",
	"inst": "Fundación Instituto Tecnológico Rafaela",
	"saldo": 15860.23,
	"act": True,
}

print(datos_personales["nya"])
print(datos_personales["act"])
