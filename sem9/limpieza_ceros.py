# import statistics
from statistics import mean


def depurar_lista(lista, filtro):
    lista_depurada = []

    for c in range(len(lista)):
        if (lista[c] != filtro):
            lista_depurada.append(lista[c])
    
    return lista_depurada
    # return [item for item in lista if item != 0] # comprensión (comprehension)


def calcular_media(lista):
    return mean(lista)


def mostrar_salida_formateada(media, decimales):
    if (decimales == 0):
        return f"Temperatura media del día: {media:.0f} ºC"
    elif (decimales == 1):
        return f"Temperatura media del día: {media:.1f} ºC"
    elif (decimales == 2):
        return f"Temperatura media del día: {media:.2f} ºC"
    else:
        return "ERROR: se deben especificar decimales (0, 1 o 2)"


def main():
    # Recuperando datos
    LECTURAS_SIMULADAS = [17.1, 17.3, 18.6, 20.1, 0, 21.4, 21.8, 22.3, 23.5, 0, 0, 25.2, 25.5, 24.0, 23.9, 0, 22.1, 22.1, 20.5, 0, 19.2, 19.0, 17.5, 16.5]
    
    # Filtrando ceros
    lista_final = depurar_lista(LECTURAS_SIMULADAS, 0)
    
    # Calculando media
    temperatura_media = calcular_media(lista_final)

    # Formateando salida
    print(mostrar_salida_formateada(temperatura_media, 2))


if (__name__ == "__main__"):
    main()
