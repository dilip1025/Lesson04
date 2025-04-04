import unittest
from app import greet

# filepath: c:\Users\user\Desktop\Lesson04\python-project\tests\test_main.py

class TestGreetFunction(unittest.TestCase):
    def test_greet_with_valid_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_whitespace(self):
        self.assertEqual(greet(" "), "Hello,  !")

    def test_greet_with_special_characters(self):
        self.assertEqual(greet("@lice"), "Hello, @lice!")
        self.assertEqual(greet("123"), "Hello, 123!")

    def test_greet_with_none(self):
        with self.assertRaises(TypeError):
            greet(None)

if __name__ == "__main__":
    unittest.main()