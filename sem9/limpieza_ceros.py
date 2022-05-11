def depurar_lista(lista):
    # lista_depurada = []

    # for c in range(len(lista)):
    #     if (lista[c] != 0):
    #         # lista.pop(c)
    #         lista_depurada.append(lista[c])
    
    # return lista_depurada

    return [item for item in lista if item != 0] # comprensión (comprehension)


def main():
    LECTURAS_SIMULADAS = [17.1, 17.3, 18.6, 20.1, 0, 21.4, 21.8, 22.3, 23.5, 0, 0, 25.2, 25.5, 24.0, 23.9, 0, 22.1, 22.1, 20.5, 0, 19.2, 19.0, 17.5, 16.5]
    lista_final = depurar_lista(LECTURAS_SIMULADAS)
    print(lista_final)


if (__name__ == "__main__"):
    main()
