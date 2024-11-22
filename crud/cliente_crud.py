from crud.factura_crud import leer_factura_por_cliente
from modelo.cliente import _Cliente
from tkinter import messagebox
clientes_db = []  # Lista simulando la base de datos de clientes en memoria


def obtener_historial_clientes():
    """Devuelve todos los clientes registrados."""
    return clientes_db


def crear_cliente(nombre, cedula):
    """Crea un cliente si la cédula no está registrada."""
    for cliente in clientes_db:
        if cliente.get_cedula() == cedula:
            return {"exito": False,
                    "mensaje": f"La cédula '{cedula}' ya está asociada al cliente '{cliente.get_nombre()}'."}

    nuevo_cliente = _Cliente(nombre, cedula)
    clientes_db.append(nuevo_cliente)
    return {"exito": True, "mensaje": f"Cliente '{nombre}' con cédula '{cedula}' creado exitosamente."}


def leer_cliente_por_cedula(cedula):
    """Busca un cliente por su cédula."""
    for cliente in clientes_db:
        if cliente.get_cedula() == cedula:
            return cliente
    return None


def obtener_historial_facturas(cliente):
    """Devuelve el historial de facturas de un cliente."""
    return cliente.get_facturas()




def buscar_por_cedula(cedula, ventana):
    """
    Busca las facturas asociadas a un cliente por su cédula y muestra los productos y cantidades.
    """
    cliente = leer_cliente_por_cedula(cedula)
    if not cliente:
        messagebox.showerror("Error", f"No se encontró ningún cliente con la cédula {cedula}.", parent=ventana)
        return None

    facturas = leer_factura_por_cliente(cedula)
    if not facturas:
        messagebox.showinfo("Sin Facturas", f"El cliente {cliente.get_nombre()} no tiene facturas registradas.", parent=ventana)
        return None

    # Mostrar información de las facturas
    resultado = []
    for factura in facturas:
        productos_info = "\n".join([f"{producto.get_nombre()} (Cantidad: {cantidad})"
                                    for producto, cantidad in factura.get_productos()])
        resultado.append(f"Factura del {factura.get_fecha()}:\nProductos:\n{productos_info}\nTotal: ${factura.calcular_total()}")

    # Muestra las facturas en un cuadro de diálogo
    messagebox.showinfo("Facturas del Cliente", "\n\n".join(resultado), parent=ventana)
    return resultado


