"""Testing the Calculation"""
from calculator.calculation import Calculation, Addition, Subtraction, Multiplication, Divition


def test_calculator_is_instance():
    """Testing the Calculation"""
    test = (1, 2)
    calculation = Calculation(test)
    assert isinstance(calculation, Calculation)


def test_calculation_addition():
    """Testing the addition get_result method"""
    test = (1, 2, 3)
    cal = Addition(test)
    assert cal.get_result() == 6.0


def test_calculation_subtraction():
    """Testing the subtraction get_result method"""
    test = (4, 2, 1)
    cal = Subtraction(test)
    assert cal.get_result() == 1.0


def test_calculation_multiplication():
    """Testing the multiplication get_result method"""
    test = (1, 2, 3, 4)
    cal1 = Multiplication(test)
    assert cal1.get_result() == 24.0


def test_calculaiton_divition():
    """Testing the divition get_result method"""
    test = (10, 2, 2)
    cal1 = Divition(test)
    assert cal1.get_result() == 2.5
    test1 = (10,0,1)
    cal2 = Divition(test1)
    assert cal2.get_result() == 'You cannot divided by 0'
