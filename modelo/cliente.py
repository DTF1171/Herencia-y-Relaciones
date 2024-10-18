class _Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__pedidos = []


    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_pedidos(self):
        return self.__pedidos

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def agregar_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def consultar_historial(self):
        return self.__pedidos
