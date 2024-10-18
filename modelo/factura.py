from datetime import datetime

class _Factura:
    def __init__(self, cliente):
        self.__fecha = datetime.now()
        self.__productos = []
        self.__total = 0
        self.__cliente = cliente

    # Getters
    def get_fecha(self):
        return self.__fecha

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    def get_cliente(self):
        return self.__cliente

    # Setters
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def agregar_producto(self, producto):
        self.__productos.append(producto)
        self.__total += producto.get_valor()

    def calcular_total(self):
        return self.__total

    def __str__(self):
        productos_str = "\n".join([str(p) for p in self.__productos])
        return f"Factura para {self.__cliente.get_nombre()}\nFecha: {self.__fecha}\nTotal: ${self.__total}\nProductos:\n{productos_str}"
