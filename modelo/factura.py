from datetime import datetime

class _Factura:
    def __init__(self, cliente):
        self.__fecha = datetime.now()  # Fecha de creación de la factura
        self.__productos = []  # Lista para almacenar productos y cantidades
        self.__total = 0  # Total inicial de la factura
        self.__cliente = cliente  # Cliente asociado a la factura

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

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto con una cantidad específica a la factura.
        """
        self.__productos.append((producto, cantidad))  # Guardar como una tupla (producto, cantidad)
        self.__total += producto.get_valor() * cantidad  # Incrementar el total según el precio y la cantidad

    def calcular_total(self):
        """
        Calcula y devuelve el total de la factura.
        """
        total = 0
        for producto, cantidad in self.__productos:
            total += producto.get_valor() * cantidad
        return total

    def __str__(self):
        """
        Representación en string de la factura.
        """
        productos_str = "\n".join([f"{p.get_nombre()} (Cantidad: {c}) - ${p.get_valor() * c}" for p, c in self.__productos])
        return f"Factura para {self.__cliente.get_nombre()}\n" \
               f"Fecha: {self.__fecha}\n" \
               f"Total: ${self.__total}\n" \
               f"Productos:\n{productos_str}"
