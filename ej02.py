# Ejercicio 2: Producto de almacén
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def valor_total(self):
        return self.precio * self.stock

    def __str__(self):
        return f"{self.nombre} | Precio: {self.precio:,.0f} Gs. | Stock: {self.stock}"


productos = [Producto("Arroz", 8500, 20), Producto("Aceite", 14000, 12), Producto("Azúcar", 7000, 15)]
for producto in productos:
    print(producto)
    print(f"Valor total en stock: {producto.valor_total():,.0f} Gs.\n")
