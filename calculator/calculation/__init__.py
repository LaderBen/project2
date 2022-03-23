"""These are calculation classes"""
from calculator.operations import Add, Subtract, Multiply, Divide


class Calculation:
    """calculation abstract base class"""

    def __init__(self, tuple_list: tuple):
        """constructor method"""
        self.values = Calculation.convert_args_2_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """factory method"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_2_tuple_of_float(tuple_list):
        """convert data to float tuple"""
        result = []
        for i in tuple_list:
            result.append(float(i))
        return tuple(result)


class Addition(Calculation):
    """calculation addition class"""

    def get_result(self):
        """get the addition results"""
        result = 0.0
        for i in self.values:
            result = Add.add(result, i)
        return result

class Subtraction(Calculation):
    """subtraction calculation class"""

    def get_result(self):
        """get the subtraction result"""
        result = self.values[0]
        for i in range(1, len(self.values)):
            result = Subtract.subtract(result, self.values[i])
        return result

class Multiplication(Calculation):
    """multiplication calculation class"""

    def get_result(self):
        """get the multiplication result"""
        result = 1.0
        for i in self.values:
            result = Multiply.multiply(result, i)
        return result


class Divition(Calculation):
    """divition calculation class"""

    def get_result(self):
        result = self.values[0]
        for i in range(1, len(self.values)):
            try:
                result = Divide.divide(result, self.values[i])
            except:
                return result
        return result