# UI/main_ui.py
import tkinter as tk
from ui.cliente_ui import ventana_cliente
from ui.producto_ui import ventana_producto
from ui.factura_ui import ventana_factura

def main_ui():
    root = tk.Tk()
    root.title("Sistema de Gestión de la Tienda Agrícola")

    tk.Button(root, text="Gestión de Clientes", command=ventana_cliente, width=25).pack(pady=10)
    tk.Button(root, text="Gestión de Productos", command=ventana_producto, width=25).pack(pady=10)
    tk.Button(root, text="Gestión de Facturas", command=ventana_factura, width=25).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_ui()
