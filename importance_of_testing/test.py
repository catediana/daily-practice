
#Exercise 2: Writing Basic Unit Tests

#Instruction:

#Use the unittest module in Python to create a test case for the buggy function from Exercise 1.
#Write test methods to check different scenarios (e.g., valid input, invalid input) and verify expected behavior.
import unittest   
def calculate_square(number):
    """Calculate the square of a number."""
    # Intentional bug: Incorrect calculation logic
    return number * 3  # This should be number * number

class TestCalculateSquare(unittest.TestCase):

    def test_valid_input(self):
        """Test with valid input."""
        self.assertEqual(calculate_square(2), 6)  # Buggy output
        self.assertEqual(calculate_square(3), 9)  # Buggy output
        self.assertEqual(calculate_square(-4), -12)  # Buggy output

    def test_zero_input(self):
        """Test with zero input."""
        self.assertEqual(calculate_square(0), 0)  # Correct output should be 0

    def test_invalid_input(self):
        """Test with invalid input."""
        with self.assertRaises(TypeError):
            calculate_square("string")  # Should raise TypeError

if __name__ == "__main__":
    unittest.main()