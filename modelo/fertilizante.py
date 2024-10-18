from .producto_control import _ProductoControl

class _Fertilizante(_ProductoControl):
    def __init__(self, registro_ICA, nombre, valor, frecuencia_aplicacion, ultima_aplicacion):
        super().__init__(registro_ICA, nombre, valor, frecuencia_aplicacion)
        if not ultima_aplicacion:
            raise ValueError("Debe especificar la fecha de la última aplicación.")
        self.__ultima_aplicacion = ultima_aplicacion

    # Getters
    def get_ultima_aplicacion(self):
        return self.__ultima_aplicacion

    # Setters
    def set_ultima_aplicacion(self, ultima_aplicacion):
        if not ultima_aplicacion:
            raise ValueError("Debe especificar la fecha de la última aplicación.")
        self.__ultima_aplicacion = ultima_aplicacion

    def __str__(self):
        return f"Fertilizante {self.get_nombre()} - ${self.get_valor()} - Última Aplicación: {self.__ultima_aplicacion}"

