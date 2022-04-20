from random import choice


OPORTUNIDADES = 3
CTD_DIGITOS_CLAVE = 8
CARACTERES_VALIDOS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789%&*!#@"


clave = ""
intentos = 1


for c in range(CTD_DIGITOS_CLAVE):
    caracter = choice(CARACTERES_VALIDOS)
    clave = clave + caracter


print("Clave generada al azar:", clave)

while (intentos <= OPORTUNIDADES):
    ingreso = input("Ingresar clave (" + str(intentos) + " de " + str(OPORTUNIDADES) + "): ")
    
    if (ingreso == clave):
        print("La clave ingresada es correcta")
        break
    else:
        print("Clave incorrecta")
    
    intentos = intentos + 1


if (intentos > OPORTUNIDADES):
    print("Se agotaron los intentos, no se ha ingresado una clave correcta")
