from modelo.factura import _Factura
from modelo.producto import _Producto
from modelo.cliente import _Cliente

# Lista para almacenar todas las facturas (en memoria)
facturas_db = []

def crear_factura(cliente, productos, cantidades):
    """
    Crea una factura para el cliente con los productos y cantidades especificados.
    """
    factura = _Factura(cliente)  # Crear una nueva factura vinculada al cliente

    # Asociar productos y cantidades a la factura
    for producto, cantidad in zip(productos, cantidades):
        factura.agregar_producto(producto, cantidad)

    # Agregar la factura a la base de datos en memoria
    facturas_db.append(factura)

    # Asociar la factura al cliente
    cliente.agregar_pedido(factura)

    return factura

def leer_factura_por_cliente(cedula):
    """
    Busca todas las facturas de un cliente por su cédula.
    """
    return [factura for factura in facturas_db if factura.get_cliente().get_cedula() == cedula]

def obtener_todas_las_facturas():
    """
    Devuelve todas las facturas almacenadas en el sistema.
    """
    return facturas_db
