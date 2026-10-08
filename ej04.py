# Ejercicio 4: Libro de biblioteca
class Libro:
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"


libro1 = Libro("El principito", "Antoine de Saint-Exupéry", True)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)
print(libro1)
print(libro2)
