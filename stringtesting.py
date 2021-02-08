import unittest
import stringadd

class averageTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(stringadd.addstrings("kevin", "pfeil"), "kevin pfeil")
        self.assertFalse(stringadd.addstrings(123, "wooop"))
        self.assertEqual(stringadd.addstrings("Kevin", "  Pfeil"), "Kevin   Pfeil")

if __name__ == "__main__":
    unittest.main()