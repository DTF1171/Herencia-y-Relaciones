# crud/cliente_crud.py
from modelo.cliente import _Cliente
from crud.factura_crud import crear_factura, leer_factura_por_cliente

clientes_db = []


def crear_cliente(nombre, cedula):
    """Crea un cliente y lo agrega a la base de datos."""
    cliente = _Cliente(nombre, cedula)
    clientes_db.append(cliente)
    return cliente


def leer_cliente_por_cedula(cedula):
    """Busca un cliente por su cédula."""
    for cliente in clientes_db:
        if cliente.get_cedula() == cedula:
            return cliente
    return None


def buscar_por_cedula(cedula):
    """Obtiene las facturas de un cliente por su cédula y muestra los productos vendidos."""
    cliente = leer_cliente_por_cedula(cedula)
    if not cliente:
        print(f"No se encontró ningún cliente con la cédula {cedula}.")
        return None

    facturas = leer_factura_por_cliente(cedula)
    if not facturas:
        print(f"El cliente {cliente.get_nombre()} no tiene facturas registradas.")
        return None

    print(f"Facturas de {cliente.get_nombre()}:")
    for factura in facturas:
        print(f"Fecha: {factura.get_fecha()}, Total: ${factura.calcular_total()}")
        print("Productos:")
        for producto in factura.get_productos():
            print(f" - {producto}")
    return facturas
