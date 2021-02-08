import unittest
import average

class averageTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(average.average([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertFalse(average.average([]))
        self.assertFalse(average.average(['kevin', 5, 7]))

if __name__ == "__main__":
    unittest.main()