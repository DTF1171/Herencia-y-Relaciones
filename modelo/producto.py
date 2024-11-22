class _Producto:
    def __init__(self, registro_ICA, nombre, valor, cantidad, tipo=None):
        self.registro_ICA = registro_ICA
        self.nombre = nombre
        self.valor = valor
        self.cantidad = cantidad  # Asegúrate de que la cantidad esté definida correctamente
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre

    def get_valor(self):
        return self.valor

    def get_cantidad(self):
        return self.cantidad  # Asegúrate de que el atributo se acceda correctamente

    def get_tipo(self):
        return self.tipo  # Método para devolver el tipo del producto

    # Setters
    def set_registro_ICA(self, registro_ICA):
        self.__registro_ICA = registro_ICA

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_valor(self, valor):
        if valor <= 0:
            raise ValueError("El valor del producto debe ser positivo.")
        self.__valor = valor

    def __str__(self):
        return f"{self.__nombre} - ${self.__valor}"
