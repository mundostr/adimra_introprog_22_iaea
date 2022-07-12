import time

# Este es un formato standard de fecha y hora (datetime) utilizado en muchos sistemas,
# por ejemplo en bases de datos Mysql
FORMATO_FYH = "%Y-%m-%dT%H:%M:%S"

fecha_original = "2022-07-06T20:35:30.859Z"
# fecha_extraida es una lista que contiene las partes e la cadena que salen de separar la original en el punto.
fecha_extraida = fecha_original.split(".")

# Se parsea el primer elemento de fecha_extraida
fecha = time.strptime(fecha_extraida[0], FORMATO_FYH)
fechaConvertida = f"La cadena original {fecha_original}, se parsea como {fecha.tm_mday}/{fecha.tm_mon}/{fecha.tm_year} a las {fecha.tm_hour}:{fecha.tm_min}"

print(fechaConvertida)
