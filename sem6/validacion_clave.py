MAX_INTENTOS = 3
CL_INTERNA = "123Abcde"


usuarioValidado = False


for intentos in range(MAX_INTENTOS): # solo permitimos MAX_INTENTOS intentos
	clave = input("Ingresar clave: ")
	if (clave == CL_INTERNA):
		usuarioValidado = True # usuarioValidado es en este caso un flag o indicador verdadero / falso
		print("Clave correcta")
		break
	else:
		print("Clave incorrecta")


# De acuerdo a cómo haya quedado "usuarioValidado", si en verdadero o en falso, mostramos mensaje
if(usuarioValidado == True):
	print("SISTEMA OK")
else:
	print("SISTEMA BLOQUEADO")
