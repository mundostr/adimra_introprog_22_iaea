"""
Introducción a colecciones de datos en Python (matrices o arrays)
Tipos habituales de colecciones:

1) Listas (corchetes) = mutable (modificable)
2) Tuplas (paréntesis) = inmutable (inmodificable)

Cómo identifico a los elementos dentro de la colección?: a través de un índice

3) Diccionarios (llaves) = parcialmente mutable (parcialmente modificable)
"""

# Variable unitaria
intentos = 18

# Lista
lecturas = [15, 12, 1, 18, 8, 21, 7, -3, 19, 13, 11, 5, 17, 6, 4, 10, 9, 2, 16]
lista2 = ["Carlos", "Pepe", "Gabriela"]

# Tupla
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Diccionario
datos_personales = {
    "apellido": "Perez",
    "nombre": "Juan",
    "edad": 23,
    "direccion": "Calle falsa 123",
    "activo": True
}


# print(intentos)
# print(lecturas)
# print(lecturas[5])
# print(dias)
# print(dias[1])

# print(lecturas[6])
# print(lecturas[-1]) # Ultimo item de la lista
# print(datos_personales)
# print(datos_personales["apellido"])

# print(lecturas)
# lecturas.append(25)


# menor = 1000
# mayor = -1000
# for c in range(len(lecturas)):
#     if lecturas[c] < menor:
#         menor = lecturas[c]
#     elif lecturas[c] > mayor:
#         mayor = lecturas[c]
# print(menor)
# print(mayor)

# lecturas.sort(reverse=True)
# print(lecturas)
# print("Menor:", lecturas[-1])
# print("Mayor:", lecturas[0])

# lista2.append("Carolina")
# lista2.sort(reverse=True)
# print(lista2)

print(lecturas)
print(lecturas[2:5])