import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Group all unit tests for the SimpleCalculator class."""

    def setUp(self):
        """
        This method runs before every individual test.
        We create a fresh SimpleCalculator instance so tests don’t
        interfere with each other by sharing state.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Verify that add(a, b) returns a + b for various inputs."""
        # Simple positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Adding zeros should still give zero
        self.assertEqual(self.calc.add(0, 0), 0)
        # Adding floats
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        # Adding negatives
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        """Verify that subtract(a, b) returns a - b for various inputs."""
        # Simple positive integers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Subtracting from zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Using floats
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        # Subtraction of two negatives
        self.assertEqual(self.calc.subtract(-3, -2), -1)

    def test_multiplication(self):
        """Verify that multiply(a, b) returns a * b for various inputs."""
        # Basic integer multiplication
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Multiplying by zero yields zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Float × integer
        self.assertAlmostEqual(self.calc.multiply(1.5, 2), 3.0)
        # Negative × positive
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_division(self):
        """Verify that divide(a, b) handles normal and edge cases."""
        # Normal integer division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Division that results in a float
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # Division by zero should return None (not an exception)
        self.assertIsNone(self.calc.divide(10, 0))
        # Zero divided by zero is also None by our implementation
        self.assertIsNone(self.calc.divide(0, 0))
        # Negative numerator
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Float ÷ float
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)

if __name__ == '__main__':
    # This will run all test methods when this script is executed directly.
    unittest.main()
