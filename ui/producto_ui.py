# UI/producto_ui.py
import tkinter as tk
from tkinter import messagebox
from crud.producto_crud import crear_producto

def ventana_producto():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")

    def crear_producto_action():
        tipo = entry_tipo.get()
        nombre = entry_nombre.get()
        valor = float(entry_valor.get())
        registro_ICA = entry_registro.get()

        producto = crear_producto(tipo, registro_ICA=registro_ICA, nombre=nombre, valor=valor,
                                  frecuencia_aplicacion=entry_frecuencia.get(),
                                  ultima_aplicacion=entry_ultima_aplicacion.get(),
                                  periodo_carencia=entry_periodo.get(),
                                  dosis=entry_dosis.get(),
                                  tipo_animal=entry_tipo_animal.get())
        messagebox.showinfo("Éxito", f"{tipo.capitalize()} '{nombre}' creado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_valor.delete(0, tk.END)

    # Widgets
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

    tk.Label(ventana, text="Frecuencia Aplicación (Producto Control):").grid(row=4, column=0)
    entry_frecuencia = tk.Entry(ventana)
    entry_frecuencia.grid(row=4, column=1)

    tk.Label(ventana, text="Última Aplicación (Fertilizante):").grid(row=5, column=0)
    entry_ultima_aplicacion = tk.Entry(ventana)
    entry_ultima_aplicacion.grid(row=5, column=1)

    tk.Label(ventana, text="Período de Carencia (Plaguicida):").grid(row=6, column=0)
    entry_periodo = tk.Entry(ventana)
    entry_periodo.grid(row=6, column=1)

    tk.Label(ventana, text="Dosis (Antibiótico):").grid(row=7, column=0)
    entry_dosis = tk.Entry(ventana)
    entry_dosis.grid(row=7, column=1)

    tk.Label(ventana, text="Tipo Animal (Antibiótico):").grid(row=8, column=0)
    entry_tipo_animal = tk.Entry(ventana)
    entry_tipo_animal.grid(row=8, column=1)

    tk.Button(ventana, text="Crear Producto", command=crear_producto_action).grid(row=9, columnspan=2, pady=10)
