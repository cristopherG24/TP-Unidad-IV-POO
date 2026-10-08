# Ejercicio 13: Habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, tarifa_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_noche = tarifa_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print("No se puede ocupar: la habitación ya está ocupada.")
        else:
            self.ocupada = True
            print("Habitación ocupada correctamente.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print("Habitación liberada.")
        else:
            print("La habitación ya está libre.")

    def costo_estadia(self, noches):
        if noches <= 0:
            print("La cantidad de noches debe ser positiva.")
            return 0
        return self.tarifa_noche * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: {self.tarifa_noche:,.0f} Gs./noche | Estado: {estado}"


habitacion = Habitacion(205, "Doble", 250000)
print(habitacion)
habitacion.ocupar()
print(habitacion)
habitacion.ocupar()
print(f"Costo por 3 noches: {habitacion.costo_estadia(3):,.0f} Gs.")
habitacion.liberar()
print(habitacion)
