class _Producto:
    def __init__(self, registro_ICA, nombre, valor):
        if valor <= 0:
            raise ValueError("El valor del producto debe ser positivo.")
        self.__registro_ICA = registro_ICA
        self.__nombre = nombre
        self.__valor = valor

    # Getters
    def get_registro_ICA(self):
        return self.__registro_ICA

    def get_nombre(self):
        return self.__nombre

    def get_valor(self):
        return self.__valor

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
