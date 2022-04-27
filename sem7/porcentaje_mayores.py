NRO_OBJ = 18


porcentaje = 0
ctd_mayores = 0
lecturas = [22, 15, 18, 21, 19, 20, 17, 16, 13, 14, 5]


ctd_lecturas = len(lecturas)

for c in range(ctd_lecturas - 1):
    if lecturas[c] > NRO_OBJ:
        ctd_mayores = ctd_mayores + 1 # ctd_mayores += 1

porcentaje = int((ctd_mayores / ctd_lecturas) * 100)

    
print(ctd_lecturas)
print(ctd_mayores)
print(porcentaje)
