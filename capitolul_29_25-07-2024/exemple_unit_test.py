import unittest
from functii import *


# in metodele din clasa de Test de functii, numele metodei de test trebuie sa inceapa neaparat cu test **CONVENTIE**

class Testfunctii(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Va fi o instructiune executata o singura data, la inceput. Nu se executa la fiecare test in parte")

    def setUp(self):
        print("Instructiuni executate inainte de fiecare test in parte, la inceput")

    def test_adunare(self):
        x = 10
        y = 5
        z = 15
        print(f"Se verifica daca adunarea dintre {x} + {y} este egala cu {z}")
        self.assertEqual(adunare(x, y), z, "Cele doua valori nu sunt egale")
        print("Testul test_adunare a fost executat cu success")

    def test_scadere(self):
        self.assertEqual(scadere(31, 18), 13, "Scaderea dintre cele 2 valori nu este corecta")
        print("Testul test_scadere a fost executat cu success")

    def test_impartire(self):
        self.assertNotEqual(impartire(30, 6), 5.1, "Impartirea dintre cele doua valori nu este corecta")
        print("Testul test_impartire a fost executat cu success")

    def test_inmultire(self):
        a = 6.0
        b = 7
        self.assertEqual(inmultire(a, b), 42)
        self.assertTrue(type(a) == float, msg=f"Variabila a cu valoarea {a} nu este de tip float")
        print("Testul test_inmultire a fost executat cu success")

    def test_ridicare_la_putere(self):
        x = 5
        y = 3
        self.assertEqual(x_la_puterea_y(x, y), 125)
        print("Testul test_ridicare_la_putere a fost executat cu success")

    def tearDown(self):
        print("Instructiune executata 1 singura data la sfarsitul fiecaruit test")

    @classmethod
    def tearDownClass(cls):
        print("Instructiunea executata 1 singura data la sfarsitul executatorii tuturor testelor, nu la finalul fiecarui test in parte")
