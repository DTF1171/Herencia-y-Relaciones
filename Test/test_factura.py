import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from modelo.cliente import _Cliente
from modelo.fertilizante import _Fertilizante
from modelo.antibiotico import _Antibiotico
from modelo.factura import _Factura


class TestFactura(unittest.TestCase):

    def test_agregar_productos_y_calcular_total(self):
        # Crear cliente
        cliente = _Cliente("Juan Perez", "123456789")

        # Crear productos
        fertilizante = _Fertilizante("ICA001", "Fertilizante X", 50000, "30 días", "01/10/2024")
        antibiotico = _Antibiotico("ICA002", "Antibiótico Bovino", 30000, 500, "Bovino")  # Verifica el uso aquí

        # Crear factura
        factura = _Factura(cliente)
        factura.agregar_producto(fertilizante)
        factura.agregar_producto(antibiotico)

        # Validar el total
        self.assertEqual(factura.calcular_total(), 80000)

    def test_factura_vacia(self):
        cliente = _Cliente("Pedro Gomez", "987654321")
        factura = _Factura(cliente)

        # Verificar que el total es 0 cuando no hay productos

        self.assertEqual(factura.calcular_total(), 0)


if __name__ == "__main__":
    unittest.main()
