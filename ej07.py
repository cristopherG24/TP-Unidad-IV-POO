# Ejercicio 7: Control de stock con alertas
class ProductoStock:
    def __init__(self, nombre, stock, stock_minimo):
        self.nombre = nombre
        self.__stock = max(0, stock)
        self.stock_minimo = max(0, stock_minimo)

    def verificar_stock(self):
        if self.__stock < self.stock_minimo:
            print(f"ALERTA: Reponer {self.nombre}. Stock por debajo del mínimo.")

    def ingresar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a ingresar debe ser positiva.")
            return
        self.__stock += cantidad
        print(f"Ingresaron {cantidad} unidades.")
        self.verificar_stock()

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser positiva.")
        elif cantidad > self.__stock:
            print("Venta rechazada: stock insuficiente.")
        else:
            self.__stock -= cantidad
            print(f"Se vendieron {cantidad} unidades.")
        self.verificar_stock()

    def __str__(self):
        return f"{self.nombre} | Stock: {self.__stock} | Mínimo: {self.stock_minimo}"


producto = ProductoStock("Leche", 10, 5)
print(producto)
producto.vender(7)
print(producto)
producto.vender(8)
print(producto)
producto.ingresar(10)
print(producto)
