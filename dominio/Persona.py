# INTEGRANTES:
# MERO SARCOS CAROLINE THALIA
# QUIÑONEZ JAIME SERGIO AURELIO
# QUIÑONEZ RONQUILLO ODALYS RAQUEL
# VILLACIS CBOHORQUEZ MICHAEL ROBERT
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.numero_libros = numero_libros
        self.activo = activo
        self.carrera = carrera

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_numero_libros(self):
        return self.numero_libros

    def set_numero_libros(self, numero_libros):
        self.numero_libros = numero_libros

    def is_activo(self):
        return self.activo

    def set_activo(self, activo):
        self.activo = activo

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera

    @abstractmethod
    def pedir_libro(self):
        return True

    @abstractmethod
    def devolver_libro(self):
        return True

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido}\nCédula: {self.cedula}\nEmail: {self.email}\nTeléfono: {self.telefono}\nDirección: {self.direccion}\nNúmero de libros: {self.numero_libros}\nActivo: {self.activo}\nCarrera: {self.carrera}"