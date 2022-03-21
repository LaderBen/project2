"""These are the Operation Classes"""


class Addition:
    """This is the addition class"""

    @staticmethod
    def add(value_1, value_2):
        """This is the add method"""
        return value_1 + value_2


class Subtraction:
    """This is the subtraction class"""

    @staticmethod
    def subtract(value_1, value_2):
        """subtract method"""
        return value_1 - value_2


class Multiplication:
    """This is the Multiplication class"""

    @staticmethod
    def multiply(value_1, value_2):
        """multiply method"""
        return value_1 * value_2

class Divition:
    """This is the Divition class"""

    @staticmethod
    def divide(value_1,value_2):
        """This is the divide method"""
        try:
            result = value_1 / value_2
        except ZeroDivisionError:
            return 'You cannot divided by 0'
        return result