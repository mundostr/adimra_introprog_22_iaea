"""
EJERCICIO RONDA DE PERSONAS
Agregados:
- Detectar cuenta divisible por 11 y saltar 1 persona, siguiendo mismo sentido de giro
Ej, si está contando horario la persona 8, la siguiente en contar deberá ser la 10; si es antihorario, la 6

- Permitir ingresar ctd de personas en ronda y límite de cuenta por consola, en lugar de indicarlos de forma fija

- Si el límite de cuenta es menor a la cantidad de personas en la ronda, no efectuar la cuenta, solo mostrar
en su lugar un mensaje de error con print
"""


import config


# tipado dinámivo vs estático
cuenta = int(0) # tipado estático
persona = 0 # tipado dinámico
giro = "horario"


for ciclo in range(config.LIMITE_CUENTA):
	# if (config.LIMITE_CUENTA < config.PERSONAS):
	#     print("Límite de cuenta menor a la cantidad de personas en la ronda")
	#     break

	cuenta = cuenta + 1 # se aumenta en 1 contador general

	if (giro == "horario"):
		if (persona == config.PERSONAS):
			persona = 0
		persona = persona + 1 # se suma 1 a contador de persona
	else:
		if (persona == 1):
			persona = config.PERSONAS + 1
		persona = persona - 1 # se resta 1 a contador de persona
		
	print(persona, cuenta)
		
	if (cuenta % 8 == 0): # cuenta es perfectamente divisible por 8
		if (giro == "horario"):
			giro = "antihorario"
		else:
			giro = "horario"

	elif (cuenta % 11 == 0): # cuenta es perfectamente divisible por 11
		if (giro == "horario"):
			persona = persona + 1
		else:
			persona = persona - 1
