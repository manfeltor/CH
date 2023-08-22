from main1cnfg import set_user_type, set_rank, newart


class PageUser:

	def __init__(self, nombre, apellido, edad, pais, mail, tipo_usuario: int,  rango: int = 0):

		self.name = nombre
		self.lName = apellido
		self.age = edad
		self.country = pais
		self.mail = mail
		self.rank = set_rank(rango, tipo_usuario)
		self.user_type = set_user_type(tipo_usuario)

	def describir(self):

		if self.user_type == 1:
			usu = "cliente"
		elif self.user_type == 2:
			usu = "seller"
		else:
			usu = "admin-dev"

		if self.rank == 1:
			ran = " con cargo ejecutivo"
		elif self.rank == 2:
			ran = " con cargo de manager"
		elif self.rank == 0:
			ran = ""
		else :
			ran = " con cargo corporativo"

		return print(f"\n{self.name} {self.lName} es un {usu}{ran}, tiene {self.age} años y reside en {self.country}")


class Cliente(PageUser):

	def __init__(self,nombre, apellido, edad, pais, mail, ultima_sucursal):
		super().__init__(nombre, apellido, edad, pais, mail, tipo_usuario=1, rango=0)
		self.artcl = {}
		self.tfact = 0
		self.ultsuc = ultima_sucursal

	def comprar(self, articulo, precio, cantidad: int = 1):
		self.artcl = newart(self.artcl, articulo, cantidad)
		self.tfact += precio

	def	compras(self):
		if len(self.artcl) == 0:
			return print("el cliente no ha comprado nada")
		print(f"\nel cliente {self.name} ha comprado los siguientes articulos:")
		for i in self.artcl:
			print(f"{self.artcl[i]} unidades de {i}")
		print(f"\npara un total de {self.tfact} denars macedonicos. ultima compra realizada en la sucursal {self.ultsuc}")
		print("\n")

"""Estimada,

debido a la situacion actual de la inflacion que es de publico conocimiento, me veo en la muy incomoda tarea de
actualizar mi remuneracion pretendida para el puesto de 350.000 ARP a 391.000 ARP (pesos argentinos trecientos noventa y un mil) netos
equivalentes a aproximadamente 470.000 ARP (pesos argentinos cuatrocientos setenta mil), por lo que te pido le comentes
esta situacion a la empresa.

es muy lamentable la situacion actual de inflacion, no obstante espero podamos seguir adelante con el proceso

atento ante cualquier novedad

un abrazo

JENP"""