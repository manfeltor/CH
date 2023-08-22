from main1cnfg import set_user_type, set_rank, newart


class PageUser:

	def __init__(self, nombre, apellido, edad, pais, tipo_usuario: int, mail=None, rango: int = 0):

		self.name = nombre
		self.lName = apellido
		self.age = edad
		self.country = pais
		self.mail = mail
		self.rank = set_rank(rango, tipo_usuario)
		self.user_type = set_user_type(tipo_usuario)

	def describir(self):

		if self.user_type == 1:
			usu = "cliente "
		elif self.user_type == 2:
			usu = "seller "
		else:
			usu = "admin-dev"

		if self.rank == 1:
			ran = " con cargo ejecutivo"
		elif self.rank == 2:
			ran = " con cargo de manager"
		else:
			ran = "con cargo corporativo"

		return print(f"{self.name} {self.lName} es un {usu}{ran}, tiene {self.age} años y reside en {self.country}")

class Cliente(PageUser):
	def __init__(self,nombre, apellido, edad, pais, mail, ultima_sucursal):
		super().__init__(nombre, apellido, edad, pais, mail)
		self.rank = 0
		self.user_type = 1
		self.artcl = {}
		self.tfact = 0
		self.ultsuc = ultima_sucursal

	def comprar(self, articulo, precio, cantidad: int = 1):
		self.artcl = newart(self.artcl, articulo, cantidad)
		self.tfact += precio

	def	compras(self):
		if len(self.artcl) == 0:
			return print("el cliente no ha comprado nada")
		print(f"el cliente {self.name} ha comprado los siguientes articulos:\n")
		for i in self.artcl:
			print(f"{self.artcl[i]} unidades de {i}")
		print("\n")
		print(f"para un total de {self.tfact}. ultima compra realizada en {self.ultsuc}")

