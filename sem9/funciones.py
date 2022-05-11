"""
Repaso básico de paradigmas tradicionales e intro a Programación Estructurada

Secuencial
Estructurada
POO (Programación Orientada a Objetos)

Una función no es más que un bloque de código, identificado bajo un nombre amigable, que puede
recibir parámetros y retornar valores, y que se ejecuta selectivamente cuando es llamada,
es decir, cada vez que lo necesitemos, podremos hacer el llamado a la función, utilizando su nombre,
el sistema derivará la ejecución al bloque la función, ejecutará su contenido y retornará al flujo
principal para continuar con las siguientes instrucciones.
"""


# Definiciones
def mostrar_cadena_formateada(cad):
	asteriscos = ""
	for i in range(len(cad)):
		asteriscos = asteriscos + "*"
	
	print(asteriscos)
	print(cad)
	print(asteriscos)


# Flujo principal de código
if (__name__ == "__main__"):
	# cadena = "El primer título"
	mostrar_cadena_formateada("El primer título")

	print()
	print("Sigue el programa")
	print()

	mostrar_cadena_formateada("Misma función con otro argumento")
