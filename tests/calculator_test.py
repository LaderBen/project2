"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.add(1) == 1


def test_calculator_multiply_method():
    """Testing the multiply function"""
    cal = Calculator()
    assert cal.multiply(1, 1) == 1


def test_calculator_divide_method():
    """Testing the divide method in Calculator"""
    calculator = Calculator()

    assert calculator.divide(4, 2) == 2
    assert calculator.divide(4, 0) == 'You cannot divided by 0'


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract(1) == -1
