import pytest
from app import greet
import sys
import os

# filepath: c:\Users\user\Desktop\Lesson04\python-project\tests\test_main.py

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_greet_with_valid_name():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

def test_greet_with_empty_string():
    assert greet("") == "Hello, !"

def test_greet_with_whitespace():
    assert greet(" ") == "Hello,  !"

def test_greet_with_special_characters():
    assert greet("@lice") == "Hello, @lice!"
    assert greet("123") == "Hello, 123!"

def test_greet_with_long_name():
    long_name = "A" * 1000
    assert greet(long_name) == f"Hello, {long_name}!"

def test_greet_with_mixed_case_name():
    assert greet("aLiCe") == "Hello, aLiCe!"

def test_greet_with_numeric_string():
    assert greet("42") == "Hello, 42!"

def test_greet_with_unicode_characters():
    assert greet("你好") == "Hello, 你好!"
    assert greet("😊") == "Hello, 😊!"
