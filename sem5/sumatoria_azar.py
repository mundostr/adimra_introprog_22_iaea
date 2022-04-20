# Librerías
import random as azar


# Constantes y variables
MAXIMO = 50
LIMITE_AZAR = 100


nro = 0
limite = 0


# Entradas
while (nro < 2 or nro > MAXIMO):
    nro = int(input("Ingrese número: "))

while (limite == 0 or limite > LIMITE_AZAR):
    limite = int(input("Ingrese límite: "))


# Procesos
suma_total = 0
for c in range(nro):
    valor_al_azar = azar.randint(1, LIMITE_AZAR)
    print(valor_al_azar)
    if (valor_al_azar > limite):
        suma_total = suma_total + valor_al_azar


# Salidas
print("La suma total es: ", suma_total)
