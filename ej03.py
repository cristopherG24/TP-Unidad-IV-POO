# Ejercicio 3: Empleado y su sueldo
class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self):
        return self.salario_mensual * 13  # 12 meses y aguinaldo

    def __str__(self):
        return f"{self.nombre} | Cargo: {self.cargo} | Sueldo mensual: {self.salario_mensual:,.0f} Gs."


empleado = Empleado("Laura Benítez", "Cajera", 3000000)
print(empleado)
print(f"Sueldo anual con aguinaldo: {empleado.salario_anual():,.0f} Gs.")
