# Ejercicio 12: Cuenta de servicio con planes
class LineaTelefonica:
    def __init__(self, cliente, plan_gb):
        self.cliente = cliente
        self.plan_gb = plan_gb
        self.__consumidos = 0

    def disponibles(self):
        return max(0, self.plan_gb - self.__consumidos)

    def consumir_datos(self, gb):
        if gb <= 0:
            print("El consumo debe ser positivo.")
        elif gb > self.disponibles():
            print("No se puede consumir esa cantidad: paquete agotado o saldo insuficiente.")
        else:
            self.__consumidos += gb
            print(f"Consumo registrado: {gb} GB.")
        if self.disponibles() == 0:
            print("AVISO: Se agotó el paquete de datos.")

    def __str__(self):
        return f"Línea de {self.cliente} | Plan: {self.plan_gb} GB | Consumidos: {self.__consumidos:g} GB | Disponibles: {self.disponibles():g} GB"


linea = LineaTelefonica("Carlos", 10)
print(linea)
linea.consumir_datos(6)
print(linea)
linea.consumir_datos(4)
print(linea)
linea.consumir_datos(1)
print(linea)
