"""

Ejemplo de URL:
protocolo -> https://
dominio -> api.openweathermap.org
ruta interna -> /data/2.5/
contenido -> weather
separador direccion / parámetros -> ?
parámetro (nombre=valor) -> q=rafaela
separador entre parámetros -> &units=metric
&appid=b07cceb706b36724ddaa2614cdb76af4
"""


import requests

NOMBRE_CIUDAD = "rafaela"
UNIDADES = "metric"
APPID = "b07cceb706b36724ddaa2614cdb76af4"
IDIOMA = "en"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={NOMBRE_CIUDAD}&units={UNIDADES}&appid={APPID}&lang={IDIOMA}"


solicitud = requests.get(URL)
solicitud_json = solicitud.json()

print(type(solicitud_json))
print(solicitud_json["main"])
print(solicitud_json["main"]["temp"])
print(solicitud_json["weather"][0]["description"])
