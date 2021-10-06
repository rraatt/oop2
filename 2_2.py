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

    def add(self, second):
        self.__numerator = self.__numerator * second.__denominator + second.__numerator * self.__denominator
        self.__denominator = self.__denominator * second.__denominator
        return Rational(self.__numerator, self.__denominator)

    def sub(self, second):
        self.__numerator = self.__numerator * second.__denominator - second.__numerator * self.__denominator
        self.__denominator = self.__denominator * second.__denominator
        return Rational(self.__numerator, self.__denominator)


    def mult(self, second):
        self.__numerator = self.__numerator * second.__numerator
        self.__denominator = self.__denominator * second.__denominator
        return Rational(self.__numerator, self.__denominator)

    def div(self, second):
        self.__numerator = self.__numerator * second.__denominator
        self.__denominator = self.__denominator * second.__numerator
        return Rational(self.__numerator, self.__denominator)

obj = Rational(2, 8)
obj2 = Rational(3, 12)
obj = obj.add(obj2)
print(obj.get())
print(obj.getfloat())
