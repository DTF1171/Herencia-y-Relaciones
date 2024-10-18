import unittest
from modelo.antibiotico import _Antibiotico

class TestAntibiotico(unittest.TestCase):

    def test_crear_antibiotico(self):
        antibiotico = _Antibiotico("ICA002", "Antibiótico Bovino", 30000, 500, "Bovino")
        self.assertEqual(antibiotico.get_nombre(), "Antibiótico Bovino")
        self.assertEqual(antibiotico.get_valor(), 30000)
        self.assertEqual(antibiotico.get_dosis(), 500)
        self.assertEqual(antibiotico.get_tipo_animal(), "Bovino")

    def test_dosis_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            _Antibiotico("ICA003", "Antibiótico Inválido", 30000, 700, "Bovino")

    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            _Antibiotico("ICA004", "Antibiótico Inválido", 30000, 500, "Elefante")

if __name__ == "__main__":
    unittest.main()
