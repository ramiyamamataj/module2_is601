import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1.0, 1.0) == 2.0

def test_subtraction():
    assert subtraction(2.0, 1.0) == 1.0

def test_multiplication():
    assert multiplication(2.0, 3.0) == 6.0

def test_division_positive():
    assert division(6.0, 2.0) == 3.0

def test_division_negative():
    with pytest.raises(ValueError, match="Divide by zero is not allowed."):
        division(1.0, 0.0)