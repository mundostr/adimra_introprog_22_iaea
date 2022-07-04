"""
Se utiliza la librería decouple para guardar los datos sensibles de configuración en un archivo por separado.

pip install python-decouple

Este archivo puede ser de formato ini o .env (buscar más infom sobre .env). En este ejemplo utilizamos .env.
Es importante respetar el nombre del archivo de configuración, incluyendo el punto inicial. Abrir el archivo para ver su formato.
"""


import pymysql
from decouple import config


def conectar_mysql():
	# Esta función recupera los datos desde el archivo de config, y retorna un objeto de conexión para
	# operar con la base de datos Mysql.
	return pymysql.connect(
		host=config("MYSQL_HOST"),
		database=config("MYSQL_DB"),
		user=config("MYSQL_USER"),
		password=config("MYSQL_PASSWORD")
	)
