# Ejercicio 1: Ficha de cliente
class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono}"


cliente1 = Cliente("Ana López", "4567890", "0981 123456")
cliente2 = Cliente("Pedro Gómez", "5234567", "0972 654321")
print(cliente1)
print(cliente2)
