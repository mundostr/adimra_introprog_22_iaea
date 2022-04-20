# Se importa el archivo config con otro nombre
import config as cfg
# Se importa la librería random
import random


# Se utiliza el método randint de la librería random, se accede a través de notación de puntos
nro_al_azar = random.randint(cfg.MIN, cfg.MAX)
elemento_al_azar = random.choice("abcdefghijklmnopqrstuvwxyz")

print(nro_al_azar)
print(elemento_al_azar)
print(cfg.UNA_TERCER_OPCION)
