import unittest
from modelo.producto import _Producto

class TestProducto(unittest.TestCase):

    def test_crear_producto(self):
        producto = _Producto("ICA001", "Producto Genérico", 5000)
        self.assertEqual(producto.get_registro_ICA(), "ICA001")
        self.assertEqual(producto.get_nombre(), "Producto Genérico")
        self.assertEqual(producto.get_valor(), 5000)

    def test_producto_valor_invalido(self):
        with self.assertRaises(ValueError):
            _Producto("ICA002", "Producto Inválido", -500)

if __name__ == "__main__":
    unittest.main()
