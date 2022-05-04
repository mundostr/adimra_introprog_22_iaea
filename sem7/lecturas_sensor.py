# Paquete de lecturas
CTD_LECTURAS = 9


# En este caso declaramos la matriz (array) como LISTA para poder ordenarla luego
LECTURAS = [22.7, 23.5, 23.1, 22.8, 23.1, 16.5, 17.4, 17.4, 17.8]


acumulado = 0
promedio = 0


# Con esta sintaxis recorremos fácilmente la matriz, sin preocuparnos del tamaño
for lectura in LECTURAS:
	acumulado = acumulado + lectura # acumulador

# Calculamos el promedio dividiendo el acumulado por la cantidad de lecturas
promedio = acumulado / CTD_LECTURAS


# Imprimimos el resultado
print("Promedio lecturas:", promedio)
print("Lecturas antes:", LECTURAS)

# Ordenamos la matriz de forma ascendente, así el primer item [0]
# va a contener el menor valor, y el último el mayor
LECTURAS.sort()

print("Lecturas después:", LECTURAS)
# Recordar que el índice de las matrices SIEMPRE comienza en 0
print("Lectura mínima:", LECTURAS[0])
# El índice -1 hace referencia al ULTIMO item de la matriz
print("Lectura máxima:", LECTURAS[-1])
