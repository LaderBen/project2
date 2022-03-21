""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication, Divition


class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, value_1):
        """ This is the add method"""
        self.result = Addition.add(self.result, value_1)
        return self.result

    def subtract(self, value_1):
        """ This is the subtract method"""
        self.result = Subtraction.subtract(self.result, value_1)
        return self.result

    def multiply(self, value_1, value_2):
        """This is the multiply method"""
        self.result = Multiplication.multiply(value_1, value_2)
        return self.result

    def divide(self, value_1, value_2):
        """This is the divide method"""
        self.result = Divition.divide(value_1, value_2)
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
