# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from dominio.Persona import Persona


class Docente(Persona):
    contador_docente = 0

    def __init__(self,cedula :str=None , nombre :str=None , apellido :str=None , email :str=None , telefono :str=None , direccion :str=None , numero_libros :str=None , activo :str=None , carrera :str=None , id_docente :str=None , titulo_3er_nivel :str=None , titulo_4to_nivel :str=None ):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id_docente = id_docente
        self.titulo_3er_nivel = titulo_3er_nivel
        self.titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1

    def get_id_docente(self):
        return self.id_docente

    def set_id_docente(self, id_docente):
        self.id_docente = id_docente

    def get_titulo_3er_nivel(self):
        return self.titulo_3er_nivel

    def set_titulo_3er_nivel(self, titulo_3er_nivel):
        self.titulo_3er_nivel = titulo_3er_nivel

    def get_titulo_4to_nivel(self):
        return self.titulo_4to_nivel

    def set_titulo_4to_nivel(self, titulo_4to_nivel):
        self.titulo_4to_nivel = titulo_4to_nivel

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True