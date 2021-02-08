import unittest
import volume

class volumeTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(volume.volume(2, 3, 4), 24)
        self.assertFalse(volume.volume("string", 2, 4))
        self.assertFalse(volume.volume(-3, 4, 5))

if __name__ == "__main__":
    unittest.main()