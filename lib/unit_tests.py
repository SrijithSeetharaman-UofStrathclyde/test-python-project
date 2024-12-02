import unittest
from methods import add, subtract, multiply, divide, lcm, hcf

class TestMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(1, -1), -1)
        with self.assertRaises(NameError) as context:  # Check for the specific exception type
            divide(5, 0)
        self.assertIn("Cannot divide by zero", str(context.exception)) # Check the exception message

    def test_lcm(self):
        self.assertEqual(lcm(2,3), 6)
        self.assertEqual(lcm(0,5), 0)
        self.assertEqual(lcm(10,25), 50)

    def test_hcf(self):
        self.assertEqual(hcf(10, 15), 5)
        self.assertEqual(hcf(0,5), 0)
        self.assertEqual(hcf(36, 60), 12)


if __name__ == '__main__':
    unittest.main()
