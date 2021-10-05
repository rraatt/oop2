class Rectangle:
    def __init__(self):
        self.__lenght = 0
        self.__height = 0

    def setter(self, a, b):
        if (0 < a < 20) and (0 < b < 20):
            # Check if values are in allowed range.
            self.__lenght = a
            self.__height = b
        else:
            raise ValueError("Values out of range!")

    def getter(self):
        return self.__lenght, self.__height

    def per(self):
        return sum(self.getter())*2
    # Returns sum of two sides multiplied by two.

    def area(self):
        var = self.getter()
        return var[0]*var[1]
    # Returns result of multiplication of two sides


obj = Rectangle()
obj.setter(10.1, 15)
print(obj.getter())
print(obj.per())
print(obj.area())
