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


RUTA = "sem8/contenido_escritura.txt"
RUTA_CSV = "sem8/contenido_escritura.csv"
contenido = "Este es el 2do contenido que se escribirá en el archivo local\nEsta es otra línea\n"

contenido_csv = ""
lista_lecturas = [23.2, 24.5, 25.0, 26.2, 22.2]
for item in lista_lecturas:
    contenido_csv = contenido_csv + str(item) + ","


archivo = open(RUTA, "w", encoding="UTF-8") # handler / UTF-8 = Unicode, códigos internacionales acentos, eñe, etc
archivo.write(contenido)
archivo.close()
print("El archivo TXT fue grabado correctamente")

archivo = open(RUTA_CSV, "w", encoding="UTF-8") # handler / UTF-8 = Unicode, códigos internacionales acentos, eñe, etc
archivo.write(contenido_csv)
archivo.close()
print("El archivo CSV fue grabado correctamente")
