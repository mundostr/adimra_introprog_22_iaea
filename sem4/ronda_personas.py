# Constantes y variables
LIMITE_CUENTA = 25
LIMITE_PERSONAS = 8

cuenta = 0
sentido = "horario"
persona = 0


# Procesos
for ciclo in range(LIMITE_CUENTA):
	# Esto es un contador, y equivale a cuenta += 1
	cuenta = cuenta + 1
	persona = persona + 1
	
	# Si cuenta es perfectamente divisible x 8
	if (cuenta % 8 == 0):
		if (sentido == "horario"):
			sentido = "antihorario"
		else:
			sentido = "horario"
	
	# Muestro valores actuales
	print(persona, cuenta, sentido)
	
	# Si cuenta es perfectamente divisible x 11
	if (cuenta % 11 == 0):
		print("es divisible x 11")
