from time import perf_counter, sleep

from keyboard import is_pressed

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

def encender_luz(luces, indice):
	print(luces[indice]["codigo"])


if (__name__ == "__main__"):
	modo = "normal"
	luces = configurar_modo(modo)
	luz_actual = 0
	luz_ya_activada = False
	marca_cronometro = perf_counter()
	
	while(True):
		# ciclar_semaforo(luces)

		if (luz_ya_activada == False):
			encender_luz(luces, luz_actual)
			luz_ya_activada = True
			
		if (perf_counter() - marca_cronometro >= luces[luz_actual]["demora"]):
			if (luz_actual < len(luces) - 1):
				luz_actual = luz_actual + 1
			else:
				luz_actual = 0
				
			luz_ya_activada = False
			marca_cronometro = perf_counter()
		
		if (is_pressed('i') and not modo == "intermitente"):
				modo = "intermitente"
				luces = configurar_modo(modo)
				luz_actual = 0
				luz_ya_activada = False
				marca_cronometro = perf_counter()
		
		if (is_pressed('n') and not modo == "normal"):
				modo = "normal"
				luces = configurar_modo(modo)
				luz_actual = 0
				luz_ya_activada = False
				marca_cronometro = perf_counter()
		
		if (is_pressed('b') and not modo == "bloqueado"):
				modo = "bloqueado"
				luces = configurar_modo(modo)
				luz_actual = 0
				luz_ya_activada = False
				marca_cronometro = perf_counter()
