import unittest
from fibonacci_number import fibonacci_number, fibonacci_number_naive


class TestFibonacciNumber(unittest.TestCase):
    def test_small(self):
        print(fib(40))
        for n in range(8):
            print(n)
            self.assertEqual(fib(n), fibonacci_number_naive(n))


def fib(n):

    a,b = 0,1
    for i in range(n):
        #print(i)
        a,b = b,a+b

    return a


if __name__ == '__main__':
    unittest.main()

