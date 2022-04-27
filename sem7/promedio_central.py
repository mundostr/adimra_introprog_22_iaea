# Librerías
# import math
import random


# Constantes y variables
ITEMS_PROMEDIO = 5
CTD_LECTURAS = 9
suma = 0
promedio = 0
lecturas = []


# Procesos
for c in range(CTD_LECTURAS):
    lecturas.append(random.randint(50, 100))
lecturas.sort(reverse=False)

# Lectura de los 5 primeros items
# for c in range(ITEMS_PROMEDIO):
#     suma = suma + lecturas[c]
# promedio = suma / ITEMS_PROMEDIO


ctd_items_lista = len(lecturas)
# item_central = math.floor(ctd_items_lista / 2)
item_central = int(ctd_items_lista / 2)

# for c in range(item_central - 1, item_central + 2):
#    suma = suma + lecturas[c]
suma = sum(lecturas[item_central - 1:item_central + 2])


# Salidas
# print(lecturas)
# print("Promedio:", promedio)
print(lecturas)
# print(ctd_items_lista)
# print(item_central)
print(suma)
