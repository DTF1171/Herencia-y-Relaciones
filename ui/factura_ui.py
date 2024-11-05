# UI/factura_ui.py
import tkinter as tk
from tkinter import messagebox
from crud.factura_crud import crear_factura
from crud.producto_crud import leer_producto_por_nombre
from crud.cliente_crud import leer_cliente_por_cedula


def ventana_factura():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Facturas")

    def crear_factura_action():
        cedula = entry_cedula.get()
        productos_nombres = entry_productos.get().split(",")

        cliente = leer_cliente_por_cedula(cedula)
        if not cliente:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return

        productos = []
        for nombre in productos_nombres:
            producto = leer_producto_por_nombre(nombre.strip())
            if producto:
                productos.append(producto)
            else:
                messagebox.showwarning("Advertencia", f"Producto '{nombre}' no encontrado.")

        if productos:
            factura = crear_factura(cliente, productos)
            messagebox.showinfo("Éxito",
                                f"Factura creada para {cliente.get_nombre()} con total ${factura.calcular_total()}.")
        else:
            messagebox.showerror("Error", "No se pudieron agregar productos a la factura.")

    # Widgets
    tk.Label(ventana, text="Cédula del Cliente:").grid(row=0, column=0)
    entry_cedula = tk.Entry(ventana)
    entry_cedula.grid(row=0, column=1)

    tk.Label(ventana, text="Productos (separados por coma):").grid(row=1, column=0)
    entry_productos = tk.Entry(ventana)
    entry_productos.grid(row=1, column=1)

    tk.Button(ventana, text="Crear Factura", command=crear_factura_action).grid(row=2, columnspan=2, pady=10)
