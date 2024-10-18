import unittest
from modelo.plaguicida import _Plaguicida

class TestPlaguicida(unittest.TestCase):

    def test_crear_plaguicida(self):
        plaguicida = _Plaguicida("ICA003", "Plaguicida X", 35000, "20 días", 45)
        self.assertEqual(plaguicida.get_nombre(), "Plaguicida X")
        self.assertEqual(plaguicida.get_valor(), 35000)
        self.assertEqual(plaguicida.get_periodo_carencia(), 45)

    def test_periodo_carencia_invalido(self):
        with self.assertRaises(ValueError):
            _Plaguicida("ICA004", "Plaguicida Y", 36000, "20 días", -5)

if __name__ == "__main__":
    unittest.main()
