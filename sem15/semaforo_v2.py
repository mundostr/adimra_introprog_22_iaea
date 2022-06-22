from time import sleep

LUCES_NORMAL = [
	{ "codigo": f"\x1b[0;30;42m{' ':24}\x1b[0m", "demora": 3 },
	{ "codigo": f"\x1b[3;30;43m{' ':24}\x1b[0m", "demora": 1 },
	{ "codigo": f"\x1b[0;30;41m{' ':24}\x1b[0m", "demora": 3 }
]


def ciclar_semaforo(luces):
    for luz in luces:
        print(luz["codigo"])
        sleep(luz["demora"])


if (__name__ == "__main__"):
    ciclar_semaforo(LUCES_NORMAL)
