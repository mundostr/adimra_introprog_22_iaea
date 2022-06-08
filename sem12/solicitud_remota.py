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
IDIOMA = "es"

URL = f"https://api.openweathermap.org/data/2.5/weather2?q={NOMBRE_CIUDAD}&units={UNIDADES}&appid={APPID}&lang={IDIOMA}"

print(URL)


def solicitar_datos_clima(ruta):
    proceso = requests.get(ruta)

    if (proceso.status_code == 200):
        return proceso.json()
    else:
        return False


def mostrar_datos_clima(datos):
    print(datos["main"]["temp"])
    print(datos["weather"][0]["description"])


def principal():
    datos_json = solicitar_datos_clima(URL)
    if (datos_json == False):
        print("Error al solicitar datos")
    else:
        mostrar_datos_clima(datos_json)


if (__name__ == "__main__"):
    principal()
