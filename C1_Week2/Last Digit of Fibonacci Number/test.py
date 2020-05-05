
import unittest
from last_digit_of_fibonacci_number import last_digit_of_fibonacci_number, last_digit_of_fibonacci_number_naive


class TestLastDigitOfFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_fibonacci_number_naive(n),
                             last_digit_of_fibonacci_number(n))



if __name__ == '__main__':
    unittest.main()
