# crud/producto_crud.py
from modelo.fertilizante import _Fertilizante
from modelo.plaguicida import _Plaguicida
from modelo.antibiotico import _Antibiotico
from modelo.producto import _Producto

productos_db = []


def crear_producto(tipo, **kwargs):
    """Crea un producto de control (fertilizante, plaguicida o antibiótico) y lo agrega a la base de datos."""
    if tipo == "fertilizante":
        producto = _Fertilizante(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'],
                                 kwargs['frecuencia_aplicacion'], kwargs['ultima_aplicacion'])
    elif tipo == "plaguicida":
        producto = _Plaguicida(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'],
                               kwargs['frecuencia_aplicacion'], kwargs['periodo_carencia'])
    elif tipo == "antibiotico":
        producto = _Antibiotico(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'], kwargs['dosis'],
                                kwargs['tipo_animal'])
    else:
        producto = _Producto(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'])

    productos_db.append(producto)
    return producto


def leer_producto_por_nombre(nombre):
    """Busca un producto por su nombre."""
    for producto in productos_db:
        if producto.get_nombre() == nombre:
            return producto
    return None
