from time import perf_counter

if (__name__ == "__main__"):
	ESPERA = 1
	segundos = 0
	ultima_marca = perf_counter()

	while(True):
		marca_actual = perf_counter()
		if (marca_actual - ultima_marca >= ESPERA):
			segundos = segundos + 1
			print(segundos)
			ultima_marca = marca_actual
