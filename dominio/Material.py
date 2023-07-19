# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.anio = anio
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad_disponible = cantidad_disponible


    def obtener_codigo(self):
        return self.codigo

    # Setter para el atributo codigo
    def modificar_codigo(self, codigo):
        self.codigo = codigo

    # Getter para el atributo autor
    def obtener_autor(self):
        return self.autor

    # Setter para el atributo autor
    def modificar_autor(self, autor):
        self.autor = autor

    # Getter para el atributo titulo
    def obtener_titulo(self):
        return self.titulo

    # Setter para el atributo titulo
    def modificar_titulo(self, titulo):
        self.titulo = titulo

    # Getter para el atributo anio
    def obtener_anio(self):
        return self.anio

    # Setter para el atributo anio
    def modificar_anio(self, anio):
        self.anio = anio

    # Getter para el atributo editorial
    def obtener_editorial(self):
        return self.editorial

    # Setter para el atributo editorial
    def modificar_editorial(self, editorial):
        self.editorial = editorial

    # Getter para el atributo disponible
    def obtener_disponible(self):
        return self.disponible

    # Setter para el atributo disponible
    def modificar_disponible(self, disponible):
        self.disponible = disponible

    # Getter para el atributo cantidad_disponible
    def obtener_cantidad_disponible(self):
        return self.cantidad_disponible

    # Setter para el atributo cantidad_disponible
    def modificar_cantidad_disponible(self, cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible

    @abstractmethod
    def actualizar_disponibilidad(self, nueva_disponibilidad):
        self.disponible = nueva_disponibilidad