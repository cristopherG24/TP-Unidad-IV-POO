# Ejercicio 9: Turnos de consultorio
class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def atender(self):
        self.estado = "atendido"

    def __str__(self):
        return f"{self.hora} - {self.paciente} ({self.estado})"


class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print("Turnos pendientes:")
        for turno in self.turnos:
            if turno.estado == "pendiente":
                print(turno)

    def __str__(self):
        return f"Agenda del día: {len(self.turnos)} turnos registrados"


agenda = Agenda()
turno1 = Turno("Ana", "08:00")
turno2 = Turno("Luis", "08:30")
turno3 = Turno("Rosa", "09:00")
for turno in [turno1, turno2, turno3]:
    agenda.agregar_turno(turno)
print(agenda)
turno1.atender()
print(f"Atendido: {turno1}")
agenda.listar_pendientes()
