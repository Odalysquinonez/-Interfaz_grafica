# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from dominio.Material import Material

class Libro(Material):
    contador_libro = 0

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, id_libro, tipo_pasta):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id_libro = id_libro
        self.tipo_pasta = tipo_pasta
        Libro.contador_libro += 1

    def obtener_id_libro(self):
        return self.id_libro

    def modificar_id_libro(self, nuevo_id):
        self.id_libro = nuevo_id

    def obtener_tipo_pasta(self):
        return self.tipo_pasta

    def modificar_tipo_pasta(self, nuevo_tipo):
        self.tipo_pasta = nuevo_tipo

    def actualizar_disponibilidad(self, nueva_disponibilidad):
        super().actualizar_disponibilidad(nueva_disponibilidad)
