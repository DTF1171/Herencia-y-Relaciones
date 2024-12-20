import tkinter as tk
from tkinter import messagebox
from crud.cliente_crud import crear_cliente, buscar_por_cedula

def ventana_cliente():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Clientes")

    def crear_cliente_action():
        nombre = entry_nombre.get()
        cedula = entry_cedula.get()
        crear_cliente(nombre, cedula)
        messagebox.showinfo("Éxito", f"Cliente '{nombre}' creado exitosamente.")
        entry_nombre.delete(0, tk.END)
        entry_cedula.delete(0, tk.END)

    def buscar_cliente_action():
        cedula = entry_cedula.get()
        resultado = buscar_por_cedula(cedula, ventana)  # Pasamos la ventana correctamente
        if resultado["exito"]:
            messagebox.showinfo("Historial de Facturas", resultado["mensaje"], parent=ventana)

    # Widgets
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Cédula:").grid(row=1, column=0, padx=5, pady=5)
    entry_cedula = tk.Entry(ventana)
    entry_cedula.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(ventana, text="Crear Cliente", command=crear_cliente_action).grid(row=2, column=0, pady=10)
    tk.Button(ventana, text="Buscar Facturas del Cliente", command=buscar_cliente_action).grid(row=2, column=1, pady=10)

    ventana.mainloop()

