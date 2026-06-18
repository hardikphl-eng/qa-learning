# test_calculator.py

from calculator import add

def test_add():
    assert add(2, 3) == 5


def subtract(a, b):
    return a - b