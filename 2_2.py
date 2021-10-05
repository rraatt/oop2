import math


class Rational:

    def __init__(self, *values):
        if values:
            if isinstance(values[0], int) and isinstance(values[1], int):
                divisor = math.gcd(values[0], values[1])
                self.__numerator = int(values[0] / divisor)
                self.__denominator = int(values[1] / divisor)
            else:
                raise ValueError ("Only integer values allowed!")
        else:
            self.__numerator = 1
            self.__denominator = 1

    def get(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def getfloat(self):
        return self.__numerator/self.__denominator


obj = Rational(2, 8)
print(obj.get())
print(obj.getfloat())
