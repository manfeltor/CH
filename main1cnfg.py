#! python3

"""modulo de configuracion para main
Contiene las funciones modulares de los constructores de clase y metodos en main"""

def set_rank(user_rank, tusr):

	"""funcion verificadora de rangos para no clientes, excepto por la primer verificacion no esta en uso, pero sirvio
	como ejercicio para sanear variables en los atributos del constructor"""

	if tusr == 1:
		user_rank = 0
	elif user_rank in range(1, 4):
		pass
	else:
		raise ValueError("no se reconoce el rango de usuario. Los tipos posibles son 1: administrativo,\n"
						 " 2: manager, 3: corporativo, o vacio para clientes")
	return user_rank


def set_user_type(user_type):

	"""funcion verificadora de usuarios de sistema, su funcion principal es la verificacion de coherencia de logica de
	datos en el constructor de clase para el atributo "user_type" """

	if user_type not in range(1, 4):
		raise ValueError("no se reconoce el tipo de usuario. Los tipos posibles son 1: cliente,\n"
						 " 2: seller, 3: admin-dev")
	else:
		return user_type


def newart(dictMatriz, artcl, cant):

	"""esta pequeña funcion modular realiza la logica de adicion o actualizacion de articulos comprados para la funcion
	"comprar". si bien no es compleja sirvio como parctica de modularizacion anidada (si es que este termino existe XD)"""

	if artcl in dictMatriz:
		dictMatriz[artcl] += cant
	else:
		dictMatriz[artcl] = cant
	return dictMatriz
