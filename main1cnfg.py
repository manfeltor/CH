

def set_rank(user_rank, tusr):
	if tusr == 1:
		user_rank = 0
	elif user_rank in range(1, 4):
		pass
	else:
		raise ValueError("no se reconoce el rango de usuario. Los tipos posibles son 1: administrativo,\n"
											 " 2: manager, 3: corporativo, o vacio para clientes")
	return user_rank

def set_user_type(user_type):
	if user_type not in range(1, 4):
		raise ValueError("no se reconoce el tipo de usuario. Los tipos posibles son 1: cliente,\n"
						 " 2: seller, 3: admin-dev")
	else:
		return user_type


def newart(dictMatriz, artcl, cant):
	if artcl in dictMatriz:
		dictMatriz[artcl] += cant
	else:
		dictMatriz[artcl] = cant
	return dictMatriz