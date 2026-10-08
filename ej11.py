# Ejercicio 11: Estudiante y sus materias
class Estudiante:
    def __init__(self, nombre, nota_minima=3):
        self.nombre = nombre
        self.notas = {}
        self.nota_minima = nota_minima

    def registrar_nota(self, materia, nota):
        if 1 <= nota <= 5:
            self.notas[materia] = nota
        else:
            print("La nota debe estar entre 1 y 5.")

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def aprobado(self):
        return bool(self.notas) and self.promedio() >= self.nota_minima

    def __str__(self):
        detalle = "\n".join(f"{materia}: {nota}" for materia, nota in self.notas.items())
        condicion = "Aprobado" if self.aprobado() else "No aprobado"
        return f"Boletín de {self.nombre}\n{detalle}\nPromedio: {self.promedio():.2f}\nCondición: {condicion}"


estudiante = Estudiante("Sofía")
estudiante.registrar_nota("Matemática", 4)
estudiante.registrar_nota("Programación", 5)
estudiante.registrar_nota("Inglés", 3)
print(estudiante)
