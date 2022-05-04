"""
Repaso formatos interecambio habituales

txt = texto plano
csv = valores separados por coma (comma separated values)
rss = RSS (RSS feed)
xml = XML (Extended Markup Language)
json = JSON (JavaScript Object Notation)

Ej json:

{
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": "30",
    "saldo": "328500.5",
    "estado": "activo"
}
"""


import json

RUTA = "sem8/datos_personales.json"


ctrl_archivo = open(RUTA, "r", encoding="utf-8")
contenido_json = json.load(ctrl_archivo)
ctrl_archivo.close()


# print(type(contenido_json))
# print(contenido_json)

# Opción 1 formateo cadena (concatenación manual)
linea = contenido_json["nombre"] + ", " + contenido_json["apellido"] + ": edad " + str(contenido_json["edad"]) + " años"
print(linea)

# Opción 2 formateo cadena (macro f)
linea2 = f'{contenido_json["nombre"]}, {contenido_json["apellido"]}: edad {contenido_json["edad"]} años (saldo: {contenido_json["saldo"] * 0.95:.2f})'
print(type(linea2))
print(linea2)
