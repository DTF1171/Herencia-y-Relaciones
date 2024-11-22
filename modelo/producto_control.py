from .producto import _Producto

class _ProductoControl(_Producto):
    def __init__(self, registro_ICA, nombre, valor, frecuencia_aplicacion,cantidad):
        super().__init__(registro_ICA, nombre, valor,cantidad)
        if not frecuencia_aplicacion:
            raise ValueError("La frecuencia de aplicación no puede estar vacía.")
        self.__frecuencia_aplicacion = frecuencia_aplicacion



    # Getters
    def get_frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion

    # Setters
    def set_frecuencia_aplicacion(self, frecuencia_aplicacion):
        if not frecuencia_aplicacion:
            raise ValueError("La frecuencia de aplicación no puede estar vacía.")
        self.__frecuencia_aplicacion = frecuencia_aplicacion
