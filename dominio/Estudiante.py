# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from dominio.Persona import Persona


class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula :str=None , nombre :str=None , apellido :str=None , email :str=None , telefono :str=None , direccion :str=None , numero_libros :str=None , activo :str=None , carrera :str=None , id_estudiante :str=None , nivel :str=None ):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id_estudiante = id_estudiante
        self.nivel = nivel
        Estudiante.contador_estudiante += 1

    def get_id_estudiante(self):
        return self.id_estudiante

    def set_id_estudiante(self, id_estudiante):
        self.id_estudiante = id_estudiante

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        self.nivel = nivel

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True