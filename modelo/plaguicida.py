from .producto_control import _ProductoControl

class _Plaguicida(_ProductoControl):
    def __init__(self, registro_ICA, nombre, valor, frecuencia_aplicacion, periodo_carencia):
        super().__init__(registro_ICA, nombre, valor, frecuencia_aplicacion)
        if periodo_carencia <= 0:
            raise ValueError("El periodo de carencia debe ser positivo.")
        self.__periodo_carencia = periodo_carencia

    # Getters
    def get_periodo_carencia(self):
        return self.__periodo_carencia

    # Setters
    def set_periodo_carencia(self, periodo_carencia):
        if periodo_carencia <= 0:
            raise ValueError("El periodo de carencia debe ser positivo.")
        self.__periodo_carencia = periodo_carencia

    def __str__(self):
        return f"Plaguicida {self.get_nombre()} - ${self.get_valor()} - Periodo de Carencia: {self.__periodo_carencia} días"
