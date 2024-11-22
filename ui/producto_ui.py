import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from crud.producto_crud import crear_producto, obtener_historial_productos


def ventana_producto():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")

    # Función para crear un nuevo producto
    def crear_producto_action():
        tipo = entry_tipo.get()
        nombre = entry_nombre.get()
        valor = float(entry_valor.get())
        registro_ICA = entry_registro.get()

        # Obtener la cantidad de los productos
        cantidad = entry_cantidad.get()

        if not cantidad.isdigit():  # Verificar que cantidad es un número
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero.")
            return

        cantidad = int(cantidad)  # Convertir la cantidad a número entero

        # Llamada a la función crear_producto
        producto = crear_producto(tipo, registro_ICA=registro_ICA, nombre=nombre, valor=valor,
                                  cantidad=cantidad,  # Aseguramos que la cantidad se pase correctamente
                                  frecuencia_aplicacion=entry_frecuencia.get(),
                                  ultima_aplicacion=entry_ultima_aplicacion.get(),
                                  periodo_carencia=entry_periodo.get(),
                                  dosis=entry_dosis.get(),
                                  tipo_animal=entry_tipo_animal.get())

        messagebox.showinfo("Éxito", f"{tipo.capitalize()} '{nombre}' creado correctamente.")

        # Limpiar los campos después de agregar el producto
        entry_nombre.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)

        # Actualizar el catálogo después de agregar el producto
        mostrar_catalogo_action()

    # Función para mostrar el catálogo de productos en un Treeview
    def mostrar_catalogo_action():
        # Obtener todos los productos del historial
        productos = obtener_historial_productos()

        # Limpiar la tabla antes de insertar nuevos datos
        for row in treeview.get_children():
            treeview.delete(row)

        if not productos:
            messagebox.showinfo("Catálogo", "No hay productos registrados.", parent=ventana)
        else:
            # Insertar los productos en la tabla
            for producto in productos:
                treeview.insert("", tk.END, values=(producto['nombre'], producto['tipo'],
                                                    producto['precio'], producto['cantidad']))

    # Widgets para crear un producto
    tk.Label(ventana, text="Tipo de Producto:").grid(row=0, column=0)
    entry_tipo = tk.Entry(ventana)
    entry_tipo.grid(row=0, column=1)

    tk.Label(ventana, text="Nombre:").grid(row=1, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=1, column=1)

    tk.Label(ventana, text="Valor:").grid(row=2, column=0)
    entry_valor = tk.Entry(ventana)
    entry_valor.grid(row=2, column=1)

    tk.Label(ventana, text="Registro ICA:").grid(row=3, column=0)
    entry_registro = tk.Entry(ventana)
    entry_registro.grid(row=3, column=1)

    # Aquí agregamos el campo de entrada para la cantidad
    tk.Label(ventana, text="Cantidad:").grid(row=4, column=0)  # Nuevo campo para cantidad
    entry_cantidad = tk.Entry(ventana)  # Campo para ingresar la cantidad
    entry_cantidad.grid(row=4, column=1)

    tk.Label(ventana, text="Frecuencia Aplicación (Producto Control):").grid(row=5, column=0)
    entry_frecuencia = tk.Entry(ventana)
    entry_frecuencia.grid(row=5, column=1)

    tk.Label(ventana, text="Última Aplicación (Fertilizante):").grid(row=6, column=0)
    entry_ultima_aplicacion = tk.Entry(ventana)
    entry_ultima_aplicacion.grid(row=6, column=1)

    tk.Label(ventana, text="Período de Carencia (Plaguicida):").grid(row=7, column=0)
    entry_periodo = tk.Entry(ventana)
    entry_periodo.grid(row=7, column=1)

    tk.Label(ventana, text="Dosis (Antibiótico):").grid(row=8, column=0)
    entry_dosis = tk.Entry(ventana)
    entry_dosis.grid(row=8, column=1)

    tk.Label(ventana, text="Tipo Animal (Antibiótico):").grid(row=9, column=0)
    entry_tipo_animal = tk.Entry(ventana)
    entry_tipo_animal.grid(row=9, column=1)

    # Botón para crear producto
    tk.Button(ventana, text="Crear Producto", command=crear_producto_action).grid(row=10, columnspan=2, pady=10)

    # Botón para ver el catálogo de productos
    tk.Button(ventana, text="Ver Catálogo de Productos", command=mostrar_catalogo_action).grid(row=11, columnspan=2,
                                                                                               pady=10)

    # Crear Treeview para mostrar el catálogo
    treeview = ttk.Treeview(ventana, columns=("Nombre", "Tipo", "Precio", "Cantidad"), show="headings")
    treeview.heading("Nombre", text="Nombre")
    treeview.heading("Tipo", text="Tipo")
    treeview.heading("Precio", text="Precio")
    treeview.heading("Cantidad", text="Cantidad")
    treeview.grid(row=12, columnspan=2, padx=10, pady=10)

    ventana.mainloop()


