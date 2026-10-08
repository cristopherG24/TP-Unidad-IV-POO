# Ejercicio 10: Carrito de compras
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} ({self.precio:,.0f} Gs.)"


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}: {self.subtotal():,.0f} Gs."


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        self.items.append(Item(producto, cantidad))

    def calcular_total(self):
        return sum(item.subtotal() for item in self.items)

    def __str__(self):
        detalle = "\n".join(str(item) for item in self.items)
        return f"Detalle de compra:\n{detalle}\nTOTAL: {self.calcular_total():,.0f} Gs."


carrito = Carrito()
carrito.agregar_item(Producto("Cuaderno", 12000), 3)
carrito.agregar_item(Producto("Bolígrafo", 3500), 2)
print(carrito)
