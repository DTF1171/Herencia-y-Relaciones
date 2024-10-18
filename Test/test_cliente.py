import unittest
from modelo.cliente import _Cliente
from modelo.factura import _Factura
from modelo.fertilizante import _Fertilizante

class TestCliente(unittest.TestCase):

    def test_crear_cliente(self):
        cliente = _Cliente("Juan Perez", "123456789")
        self.assertEqual(cliente.get_nombre(), "Juan Perez")
        self.assertEqual(cliente.get_cedula(), "123456789")
        self.assertEqual(len(cliente.get_pedidos()), 0)

    def test_agregar_pedido(self):
        cliente = _Cliente("Juan Perez", "123456789")
        fertilizante = _Fertilizante("ICA001", "Fertilizante X", 50000, "30 días", "01/10/2024")
        factura = _Factura(cliente)
        factura.agregar_producto(fertilizante)
        cliente.agregar_pedido(factura)
        self.assertEqual(len(cliente.get_pedidos()), 1)
        self.assertEqual(cliente.get_pedidos()[0], factura)

if __name__ == "__main__":
    unittest.main()
