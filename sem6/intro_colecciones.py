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
lecturas = [15, 12, 1, 18, 8, 21, 7, 3, 19, 13, 11, 5, 17, 6, 4, 10, 9, 2, 16]

# Tupla
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Diccionario
datos_personales = {"apellido": "Pérez", "nombre": "Juan", "edad": 23, "direccion": "Calle falsa 123", "activo": True }


print(intentos)
print(lecturas)
print(lecturas[5])
print(dias)
print(dias[1])