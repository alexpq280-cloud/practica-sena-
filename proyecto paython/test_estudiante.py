import unittest
from estudiante import Estudiante


class TestEstudiante(unittest.TestCase):

    def test_agregar_nota(self):
        est = Estudiante("Juan", 20)
        est.agregar_nota(90)
        self.assertEqual(est.notas, [90])

    def test_calcular_promedio(self):
        est = Estudiante("Juan", 20)
        est.agregar_nota(80)
        est.agregar_nota(100)
        self.assertEqual(est.calcular_promedio(), 90)


if __name__ == "__main__":
    unittest.main()