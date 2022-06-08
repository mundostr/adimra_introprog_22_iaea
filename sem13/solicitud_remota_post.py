"""
Práctica con librería requests y solicitudes tipo post

Endpoint control temperatura media: http://pad19.com:3030/temperatura?sensor=33
Endpoint carga lectura: http://pad19.com:3030/cargar_sensor
"""


import requests

PROTOCOLO = "http"
HOST = "pad19.com"
PUERTO = "3030"
ENDPOINT = "cargar_sensor"
URL_API = f"{PROTOCOLO}://{HOST}:{PUERTO}/{ENDPOINT}"


def enviar_datos_sensor(parametros):
    solicitud = requests.post(URL_API, json=parametros)
    
    if (solicitud.status_code == 200):
        return solicitud.json()
    
    return False


def main():
    carga = enviar_datos_sensor({ "sensor": 33, "valor": 20.9 })
    if (carga == False):
        print("Error al cargar el sensor")
    else:
        print(carga)


if (__name__ == "__main__"):
    main()
