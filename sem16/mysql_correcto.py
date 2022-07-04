# Ver función conectar_mysql en db.py para explicación
from db import conectar_mysql

if (__name__ == "__main__"):
	# EL bloque try / except, permite interceptar errores en caso de algún mal funcionamiento, evitando
	# que el usuario simplemente observe un cuelgue del sistema y un mensaje de error general.
	try:
		ID_SENSOR = 32
		
		# Forma 1
		# Esta forma de consulta directa sin parámetros, funciona obviamente, solo se pasa una cadena SQL
		# CONSULTA = "select sensores.nombre, lecturas.media from sensores, lecturas where sensores.id = lecturas.id_sensor and sensores.id = 32 order by sensores.id asc"

		# Forma 2
		# Esta segunda forma empleando f-strings para pasar parámetros, también funciona, pero NO es la correcta
		# CONSULTA = f"select sensores.nombre, lecturas.media from sensores, lecturas where sensores.id = lecturas.id_sensor and sensores.id = {ID_SENSOR} order by sensores.id asc"

		# Forma 3
		# Esta forma de generar una sentencia SQL pasando parámetros, SI es la correcta, y evita el problema de la llamada "inyección SQL".
		# Notar el uso del placeholder %s para el id de sensor
		CONSULTA = "select sensores.nombre, lecturas.media from sensores, lecturas where sensores.id = lecturas.id_sensor and sensores.id = %s order by sensores.id asc"
		
		# La consulta no solo acepta un SQL plano, también puede contener un llamado a un procedimiento o función almacenada en la base de datos
		# CONSULTA = "call getReadingsSensor(%s)"
		
		conexion = conectar_mysql()
		gestor = conexion.cursor()
		# Si se utilizan las formas 1 o 2, el execute solo recibe el parámetro de la consulta
		# gestor.execute(CONSULTA)
		# Si se utiliza la forma correcta 3, el execute recibe la consulta y el listado de parámetros como tupla,
		# por eso el segundo parámetro encerrado a su vez entre paréntesis
		gestor.execute(CONSULTA, (ID_SENSOR))
		resultado = gestor.fetchall()
		print(resultado)
		conexion.close()
	except Exception as err:
		print(f"ERROR!: {err}")
	