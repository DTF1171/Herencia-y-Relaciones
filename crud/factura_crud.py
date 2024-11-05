# crud/factura_crud.py
from modelo.factura import _Factura
from modelo.producto import _Producto
from modelo.cliente import _Cliente

facturas_db = []

def crear_factura(cliente, productos):
    """Crea una factura para el cliente con los productos especificados."""
    factura = _Factura(cliente)
    for producto in productos:
        factura.agregar_producto(producto)
    facturas_db.append(factura)
    cliente.agregar_pedido(factura)  # Asociamos la factura al cliente
    return factura

def leer_factura_por_cliente(cedula):
    """Busca todas las facturas de un cliente por su cédula."""
    return [factura for factura in facturas_db if factura.get_cliente().get_cedula() == cedula]
