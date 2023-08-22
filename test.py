#! python3

"""archivo de prueba para la logica y funcionamiento de las clases y metodos de main"""

from main1 import Cliente as Clien

pepe = Clien("Felipe", "Torres", "32", "argentina","eluna", "tigre")
print(pepe.compras())

print(pepe.describir())

pepe.comprar("vaso", 100)
pepe.comprar("caja", 50, 3)

print(pepe.compras())

pepe.comprar("vaso", 80, 2)

print(pepe.compras())
