#Task 3

import unittest

def fizzbuzzer(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        result = fizzbuzzer(15)
        self.assertEqual(result, "FizzBuzz")

    def test_fizz(self):
        result = fizzbuzzer(3)
        self.assertEqual(result, "Fizz")

    def test_buzz(self):
        result = fizzbuzzer(5)
        self.assertEqual(result, "Buzz")

def main():
    for i in range (1, 101):
        print(fizzbuzzer(i))

if __name__ == "__main__":
    main()
