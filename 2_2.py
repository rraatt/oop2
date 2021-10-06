import math


class Rational:

    def __init__(self, *values):
        if values:
            if values[1] and isinstance(values[0], int) and isinstance(values[1], int):
                divisor = math.gcd(values[0], values[1])
                self.__numerator = values[0] // divisor
                self.__denominator = values[1] // divisor
            else:
                raise ValueError("Only integer values allowed! Second values is not zero.")
        else:
            self.__numerator = 1
            self.__denominator = 1

    def get(self):
        return f'{self.__numerator} / {self.__denominator}'

    def getfloat(self):
        return self.__numerator/self.__denominator


obj = Rational(2, 8)
print(obj.get())
print(obj.getfloat())
