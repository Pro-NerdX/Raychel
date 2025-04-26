import unittest

from utils.vec3 import Vec3

class TestVec3(unittest.TestCase):
    
    def test_div(self):
        expected = Vec3(3.0, 3.0, 3.0)
        a = Vec3(15.0, 15.0, 15.0)
        b = 5.0
        self.assertEqual(a / b, expected)
    
    def test_unit_vector_1(self):
        expected = Vec3(1.0, 0.0, 0.0)
        a = Vec3(2.0, 0.0, 0.0)
        self.assertEqual(a.norm(), expected)

    def test_unit_vector_2(self):
        expected = Vec3(1.0, 0.0, 0.0)
        a = Vec3(1.0, 0.0, 0.0)
        self.assertEqual(a.norm(), expected)

if __name__ == "__main__":
    unittest.main()
