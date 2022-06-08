from json import dumps

import requests

RUTA_LOCAL = "sem12/clasificacion_f1.json"
RUTA_REMOTA = "https://ergast.com/api/f1/2022/driverStandings.json"


def guardar_backup_local(ruta, contenido):
	with open(ruta, "w", encoding="UTF-8") as archivo: ## trunca el contenido
		archivo.write(dumps(contenido))
	print("Backup local guardado")

def recuperar_clasificacion_remota(ruta):
    proceso = requests.get(ruta)

    if (proceso.status_code == 200):
        return proceso.json()
    else:
        return False

def main():
	clasificacion = recuperar_clasificacion_remota(RUTA_REMOTA)
	guardar_backup_local(RUTA_LOCAL, clasificacion)


if __name__ == "__main__":
	main()
