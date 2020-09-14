from main import esercizio
import unittest

class TestAdd(unittest.TestCase):
    """
    Test per funzione esercizio
    """
    def test_1(self):
        """
        Test 1: ci sono due interi con il proprio opposto dovrebbe restituire il
		più piccolo
        """
        result = esercizio([8,3,-3,9,-8])
        self.assertEqual(result, 3)

    def test_2(self):
        """
        Test 2
        """
        result = esercizio([2,2,4,-2,4,-2])
        self.assertEqual(result, 2)

    def test_3(self):
        """
        Test 3: non ci sono interi con il loro opposto, dovrebbe restituire 0
        """
        result = esercizio([1,-3,-4,5,7,2])
        self.assertEqual(result, 0)

    def test_4(self):
        """
        Test 4: fuori da range, dovrebbe restituire una eccezione
        """
        with self.assertRaises(Exception): esercizio([-7,-1,8,7,9,-100001])

if __name__ == '__main__':
    unittest.main()
