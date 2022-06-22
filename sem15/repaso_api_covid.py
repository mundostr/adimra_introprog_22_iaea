import requests


def solicitar_datos(url):
	solicitud = requests.get(url)

	if (solicitud.status_code == 200):
		return solicitud.json()
	else:
		return {}


if (__name__ == "__main__"):
	URL_API = "https://api.covid19api.com/summary"

	datos = solicitar_datos(URL_API)
	ultima_actualizacion = datos["Date"]
	datos_argentina = datos["Countries"][7]

	nc = datos_argentina["NewConfirmed"]
	tc = datos_argentina["TotalConfirmed"]
	nm = datos_argentina["NewDeaths"]
	tm = datos_argentina["TotalDeaths"]
	nr = datos_argentina["NewRecovered"]
	tr = datos_argentina["TotalRecovered"]

	if (len(datos) == 0):
		print("No se pudo realizar la solicitud")
	else:
		print(f"NC: {nc} | TC: {tc} | NM: {nm} | TM: {tm} | NR: {nr} | TR: {tr}")
