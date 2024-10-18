import unittest
from modelo.fertilizante import _Fertilizante

class TestFertilizante(unittest.TestCase):

    def test_crear_fertilizante(self):
        fertilizante = _Fertilizante("ICA001", "Fertilizante A", 30000, "30 días", "01/10/2023")
        self.assertEqual(fertilizante.get_nombre(), "Fertilizante A")
        self.assertEqual(fertilizante.get_valor(), 30000)
        self.assertEqual(fertilizante.get_ultima_aplicacion(), "01/10/2023")

    def test_fertilizante_ultima_aplicacion_invalida(self):
        with self.assertRaises(ValueError):
            _Fertilizante("ICA002", "Fertilizante B", 40000, "30 días", "")

if __name__ == "__main__":
    unittest.main()
