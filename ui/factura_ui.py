import tkinter as tk
from tkinter import messagebox
from crud.factura_crud import crear_factura
from crud.producto_crud import leer_producto_por_nombre
from crud.cliente_crud import leer_cliente_por_cedula


def ventana_factura():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Facturas")

    # Variables para almacenar los productos y cantidades ingresados
    productos = []
    cantidades = []

    def agregar_producto_action():
        # Obtener el nombre del producto y la cantidad de las entradas
        nombre_producto = entry_producto.get().strip()
        cantidad = entry_cantidad.get().strip()

        # Validar que se ingresen datos en ambos campos
        if not nombre_producto or not cantidad:
            messagebox.showerror("Error", "Por favor ingrese tanto el producto como la cantidad.")
            return

        # Validar si el producto existe
        producto = leer_producto_por_nombre(nombre_producto)
        if producto:
            productos.append(producto)  # Agregar el producto a la lista
            cantidades.append(int(cantidad))  # Agregar la cantidad como entero a la lista
            # Limpiar los campos para nuevos ingresos
            entry_producto.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            messagebox.showinfo("Producto agregado", f"Producto '{nombre_producto}' agregado con cantidad {cantidad}.")
        else:
            messagebox.showwarning("Producto no encontrado", f"El producto '{nombre_producto}' no existe.")

    def crear_factura_action():
        cedula = entry_cedula.get().strip()

        # Validar que se haya ingresado la cédula
        if not cedula:
            messagebox.showerror("Error", "Por favor ingrese la cédula del cliente.")
            return

        # Validar que haya productos agregados
        if not productos:
            messagebox.showerror("Error", "Debe agregar al menos un producto a la factura.")
            return

        # Validar si el cliente existe
        cliente = leer_cliente_por_cedula(cedula)
        if not cliente:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return

        # Crear la factura con los productos y cantidades
        factura = crear_factura(cliente, productos, cantidades)
        messagebox.showinfo("Factura creada", f"Factura creada para {cliente.get_nombre()} con total ${factura.calcular_total()}.")

    # Widgets
    tk.Label(ventana, text="Cédula del Cliente:").grid(row=0, column=0)
    entry_cedula = tk.Entry(ventana)
    entry_cedula.grid(row=0, column=1)

    tk.Label(ventana, text="Producto:").grid(row=1, column=0)
    entry_producto = tk.Entry(ventana)
    entry_producto.grid(row=1, column=1)

    tk.Label(ventana, text="Cantidad:").grid(row=1, column=2)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.grid(row=1, column=3)

    # Botón para agregar producto y cantidad
    tk.Button(ventana, text="Agregar Producto", command=agregar_producto_action).grid(row=2, columnspan=4, pady=10)

    # Botón para crear factura
    tk.Button(ventana, text="Crear Factura", command=crear_factura_action).grid(row=3, columnspan=4, pady=10)
