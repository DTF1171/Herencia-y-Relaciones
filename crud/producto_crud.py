from modelo.fertilizante import _Fertilizante
from modelo.plaguicida import _Plaguicida
from modelo.antibiotico import _Antibiotico
from modelo.producto import _Producto

productos_db = []  # Lista simulando la base de datos de productos

def leer_producto_por_nombre(nombre):
    """Busca un producto por su nombre en la base de datos de productos."""
    for producto in productos_db:
        if producto.get_nombre() == nombre:
            return producto
    return None
def crear_producto(tipo, **kwargs):
    """Crea un producto de control (fertilizante, plaguicida o antibiótico) y lo agrega a la base de datos."""
    if tipo == "fertilizante":
        # Verifica que se pasen solo los 6 parámetros necesarios
        producto = _Fertilizante(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'],
                                 kwargs['frecuencia_aplicacion'], kwargs['ultima_aplicacion'], kwargs['cantidad'])
    elif tipo == "plaguicida":
        producto = _Plaguicida(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'],
                               kwargs['frecuencia_aplicacion'], kwargs['periodo_carencia'], kwargs['cantidad'])
    elif tipo == "antibiotico":
        producto = _Antibiotico(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'], kwargs['dosis'],
                                kwargs['tipo_animal'], kwargs['cantidad'])
    else:
        producto = _Producto(kwargs['registro_ICA'], kwargs['nombre'], kwargs['valor'], kwargs['cantidad'])

    productos_db.append(producto)
    return producto



def obtener_historial_productos():
    """Devuelve todos los productos registrados."""
    productos_info = []
    for producto in productos_db:
        productos_info.append({
            "nombre": producto.get_nombre(),
            "tipo": producto.get_tipo(),
            "precio": producto.get_valor(),
            "cantidad": producto.get_cantidad()  # Llamamos al método get_cantidad() para obtener la cantidad
        })
    return productos_info
