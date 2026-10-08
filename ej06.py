# Ejercicio 6: Cuenta corriente de un comercio
class CuentaCorriente:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.__saldo = max(0, saldo)

    def acreditar(self, monto):
        if monto <= 0:
            print("No se puede acreditar un monto no positivo.")
            return
        self.__saldo += monto
        print(f"Acreditación: {monto:,.0f} Gs.")

    def consumir(self, monto):
        if monto <= 0:
            print("El consumo debe ser positivo.")
        elif monto > self.__saldo:
            print(f"Compra rechazada: saldo insuficiente para {monto:,.0f} Gs.")
        else:
            self.__saldo -= monto
            print(f"Compra realizada: {monto:,.0f} Gs.")

    def __str__(self):
        return f"Cuenta de {self.cliente} | Saldo: {self.__saldo:,.0f} Gs."


cuenta = CuentaCorriente("Marcos", 50000)
print(cuenta)
cuenta.acreditar(30000)
print(cuenta)
cuenta.consumir(25000)
print(cuenta)
cuenta.consumir(100000)
print(cuenta)
