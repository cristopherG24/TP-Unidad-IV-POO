# Ejercicio 5: Vehículo de una agencia
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        return f"{self.marca} {self.modelo} {self.anio} — {self.precio:,.0f} Gs."

    def __str__(self):
        return f"Vehículo en venta: {self.descripcion_comercial()}"


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo2 = Vehiculo("Kia", "Rio", 2019, 68000000)
print(vehiculo1)
print(vehiculo2)
