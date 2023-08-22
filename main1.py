#! python3

"""Este es el archivo main para la creacion de clases y funciones de la segunda preentrega de el curso de CoderHouse.
El mismo contiene la clase padre "PageUser" y una hija "Cliente", que es en la que se enfocara el proyecto"""

from main1cnfg import set_user_type, set_rank, newart


class PageUser:
    """Esta es la clase maestra de usuarios de la plataforma.
	El tipo_usuario solo recibe valores enteros de 1 a 3 asi:
	1. cliente (es en el que se enfoca el proyecto)
	2. seller
	3. admin-dev

	Asi mismo el rango solo aceptara 4 valores:
	0. rango nulo
	1. administrativo
	2. management
	3. corporativo

	como solo vamos a usar la creacion de cliente, no hay necesidad de modificarlos ya que el constructor de esta clase
	setea tipo_usuario en 1 y rango en 0 de forma predeterminada, pero quedan como esqueleto para un proyecto mas
	completo"""

    def __init__(self, nombre, apellido, edad, pais, mail, tipo_usuario: int, rango: int = 0):

        self.name = nombre
        self.lName = apellido
        self.age = edad
        self.country = pais
        self.mail = mail
        self.rank = set_rank(rango, tipo_usuario)
        self.user_type = set_user_type(tipo_usuario)

    def describir(self):

        """esta funcion describe el usuario en leguaje natural como tipo consulta"""

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
        else:
            ran = " con cargo corporativo"

        return print(f"\n{self.name} {self.lName} es un {usu}{ran}, tiene {self.age} años y reside en {self.country}")


class Cliente(PageUser):
    """esta es la clase principal del proyecto, ya que es la que administra clientes, hereda de PageUser.

	como solo vamos a usar la creacion de cliente, no hay necesidad de modificarlos ya que el constructor de esta clase
	setea tipo_usuario en 1 y rango en 0 de forma predeterminada, pero quedan como esqueleto para un proyecto mas
	completo

	ademas de tomar argumentos de la clase padre, setea los de tipo_usuario en 1 y rango en 0, recibe el de ultima
	sucursal de compra y genera un acumulador de articulos y cantidades compradas como diccionario y un campo que
	sumariza todas las compras realizadas, ambos campos modificados por la funcion comprar"""

    def __init__(self, nombre, apellido, edad, pais, mail, ultima_sucursal):
        super().__init__(nombre, apellido, edad, pais, mail, tipo_usuario=1, rango=0)
        self.artcl = {}
        self.tfact = 0
        self.ultsuc = ultima_sucursal

    def comprar(self, articulo, precio, cantidad: int = 1):

        """esta funcion añade articulos y cantidad (o actualiza si ya existe una compra del mismo articulo) al atributo
        acumulador de articulos "artcl" y suma el monto de la compra al acumulador de facturacion total "tfact"
        de la clase

        si no se declara cantidad de articulos comprados, cantidad se setea a 1 de forma predeterminada"""

        self.artcl = newart(self.artcl, articulo, cantidad)
        self.tfact += precio

    def compras(self):

        """esta funcion detalla el historial de compras del cliente.
        Muestra el historico de articulos y cantidades adquiridas, y el total historico facturado"""

        if len(self.artcl) == 0:
            return print("el cliente no ha comprado nada")
        print(f"\nel cliente {self.name} ha comprado los siguientes articulos:")
        for i in self.artcl:
            print(f"{self.artcl[i]} unidades de {i}")
        print(
            f"\npara un total de {self.tfact} denars macedonicos. ultima compra realizada en la sucursal {self.ultsuc}")
        print("\n")
