import pytest
from python_calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.calculate_answer(2,3,"+") == 5

def test_multiplication():
    calc = Calculator()
    assert calc.calculate_answer(2,6,"*") == 12

def test_subtraction():
    calc = Calculator()
    assert calc.calculate_answer(10, 4, "-") == 6

def test_division():
    calc = Calculator()
    assert calc.calculate_answer(20, 5, "/") == 4

def test_modulo():
    calc = Calculator()
    assert calc.calculate_answer(10, 3, "%") == 1

def test_exponent():
    calc = Calculator()
    assert calc.calculate_answer(2, 3, "**") == 8

def test_integer_division():
    calc = Calculator()
    assert calc.calculate_answer(10, 3, "//") == 3
