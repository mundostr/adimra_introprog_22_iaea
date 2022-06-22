import time

import funcy
import keyboard

LUCES = {
	"verde": { "codigo": f"\x1b[0;30;42m{' ':24}\x1b[0m", "demora": 3 },
	"amarilla": { "codigo": f"\x1b[3;30;43m{' ':24}\x1b[0m", "demora": 1 },
	"roja": { "codigo": f"\x1b[0;30;41m{' ':24}\x1b[0m", "demora": 3 },
	"apagada": { "codigo": f"{' ':24}\x1b[0m", "demora": 1 },
}
CICLO_NORMAL = ["verde", "amarilla", "roja"]
CICLO_INTERMITENTE = ["amarilla", "apagada"]


def ciclar_semaforo(luces):
	for luz in luces.values():
		print(luz["codigo"])
		time.sleep(luz["demora"])

def setear_luces(modo):
	if (modo == "normal"):
		return funcy.omit(LUCES, "apagada")
	elif (modo == "bloqueado"):
		return funcy.omit(LUCES, "verde, amarilla, apagada")
	else:
		return funcy.omit(LUCES, "verde, roja")

def main():
	modo = "normal"
	luces = setear_luces(modo)

	while(True):
		ciclar_semaforo(luces)


if (__name__ == "__main__"):
	main()
