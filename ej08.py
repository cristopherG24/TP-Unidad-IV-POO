# Ejercicio 8: Reproductor de lista de canciones
class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos, segundos = divmod(self.duracion_segundos, 60)
        return f"{self.titulo} - {self.artista} ({minutos}:{segundos:02d})"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        return sum(cancion.duracion_segundos for cancion in self.canciones)

    def __str__(self):
        detalle = "\n".join(f"- {cancion}" for cancion in self.canciones)
        minutos, segundos = divmod(self.duracion_total(), 60)
        return f"Lista: {self.nombre}\n{detalle}\nDuración total: {minutos}:{segundos:02d}"


lista = ListaReproduccion("Mis favoritas")
lista.agregar_cancion(Cancion("Canción A", "Artista A", 205))
lista.agregar_cancion(Cancion("Canción B", "Artista B", 180))
lista.agregar_cancion(Cancion("Canción C", "Artista C", 240))
print(lista)
