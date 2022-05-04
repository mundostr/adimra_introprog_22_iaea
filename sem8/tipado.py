"""
Repaso de tipado dinámico vs estático

Tipos de datos habituales en Python
int
float
bool
str
"""

n01 = int(16) # tipado estático, forzamos la asignación del valor como entero (int)
n02 = "Pedro" # tipado dinámico habitual
n03 = 322.4 # tipado dinámico habitual

print(n01)
print(type(n01))

print(n02)
print(type(n02))

print(int(n03))
print(type(n03))
