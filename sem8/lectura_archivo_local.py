"""
Repaso de gestión básica de archivos locales (lectura / escritura)

ruta / path = ubicación del archivo

Ejs rutas ABSOLUTAS:
Ej Windows: C:/programacion/pruebas/python/archivos_locales.py
Ej Linux / Mac: /home/cperren/programacion/python/archivos_locales.py

Ejs rutas RELATIVAS:
sem8/archivos_locales.py

Modos básicos de apertura:
r = read (solo lectura)
w = write (escritura, trunca el contenido)
a = append (escritura, añade al contenido)
"""


RUTA = "sem8/contenido.txt"


archivo = open(RUTA, "r", encoding="UTF-8") # handler / UTF-8 = Unicode, códigos internacionales acentos, eñe, etc
contenido = archivo.read()
archivo.close()


print(contenido)
