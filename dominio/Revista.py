# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from Material import Material

class Revista(Material):
    contador_revista = 0

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id_revista, tipo):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id_revista = id_revista
        self.tipo = tipo
        Revista.contador_revista += 1

    def obtener_id_revista(self):
        return self.id_revista

    def modificar_id_revista(self, nuevo_id):
        self.id_revista = nuevo_id

    def obtener_tipo(self):
        return self.tipo

    def modificar_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo

    def actualizar_disponibilidad(self, nueva_disponibilidad):
        super().actualizar_disponibilidad(nueva_disponibilidad)