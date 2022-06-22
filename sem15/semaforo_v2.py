from time import sleep

LUCES_NORMAL = [
	{ "codigo": f"\x1b[0;30;42m{' ':24}\x1b[0m", "demora": 3 },
	{ "codigo": f"\x1b[3;30;43m{' ':24}\x1b[0m", "demora": 1 },
	{ "codigo": f"\x1b[0;30;41m{' ':24}\x1b[0m", "demora": 3 }
]

LUCES_INTERMITENTE = [
	{ "codigo": f"\x1b[3;30;43m{' ':24}\x1b[0m", "demora": 1 },
	{ "codigo": f"{' ':24}\x1b[0m", "demora": 1 }
]

LUCES_BLOQUEADO = [
	{ "codigo": f"\x1b[0;30;41m{' ':24}\x1b[0m", "demora": 3 }
]


def configurar_modo(modo):
	if (modo == "normal"):
		return LUCES_NORMAL
	elif (modo == "intermitente"):
		return LUCES_INTERMITENTE
	elif (modo == "bloqueado"):
		return LUCES_BLOQUEADO


def ciclar_semaforo(luces):
	for luz in luces:
		print(luz["codigo"])
		sleep(luz["demora"])


if (__name__ == "__main__"):
	modo = "normal"
	
	luces = configurar_modo(modo)

	while(True):
		ciclar_semaforo(luces)
