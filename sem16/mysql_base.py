import mysql.connector

conexion = mysql.connector.connect(host="idyd.ar", user="adimra", password="adm1727", database="adimra")

def consultar_bbdd(consulta):
	gestor = conexion.cursor()
	gestor.execute(consulta)
	resultado = gestor.fetchall()
	
	return resultado


if (__name__ == "__main__"):
	# CONSULTA = "select * from sensores order by id asc"
	CONSULTA = "select sensores.nombre, lecturas.media from sensores, lecturas where sensores.id = lecturas.id_sensor and sensores.id = 32 order by sensores.id asc"
	resultado = consultar_bbdd(CONSULTA)
	print(resultado);
