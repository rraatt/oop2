import numpy


class Student:
    """Class for storing info of students"""
    def __init__(self, name, surname, book, grades):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError('Name and Surname should be string data type!')
        if not isinstance(book, int):
            raise TypeError('Record book number should be int type')
        if not all(isinstance(x, int) for x in grades):
            raise TypeError('Grades should be int type!')
        self.name = name
        self.surname = surname
        self.book = book
        self.grades = grades

    def __str__(self):
        return f'{self.name} {self.surname}, record book number: {self.book}, average grade: {self.get_average()}'

    def get_average(self):
        """Method for calculating average score of a student"""
        return sum(self.grades)/len(self.grades)


class Group:
    """Class for storing links to students in one group and getting info about top 5 students"""
    def __init__(self):
        self.list = []
        self.students = 0

    def add_student(self, inp):
        """Method for adding a student to group, no more than 20 students in a group are allowed, input should be
        a Student type instance! """
        if self.students == 20:
            raise AssertionError('No more than 20 students in a group!')
        if not isinstance(inp, Student):
            raise TypeError('Input should be Student type!')
        self.list.append(inp)
        self.students += 1

    def top_five(self):
        """Method for getting top five students in a group, returns of list of Student type instances"""
        avg = numpy.array([x.get_average() for x in self.list])
        ids = (-avg).argsort()[:5]
        return [self.list[x] for x in ids]

    def __str__(self):
        return '\n'.join([str(x) for x in self.top_five()])


def main():
    a = Student('Anthony', 'Dzhulai', 1, [80, 81, 79, 82, 78])
    b = Student('Khrystyna', 'Petrychenko', 2, [90, 91, 89, 92, 88])
    c = Student('Vladlen', 'Khaziev', 3, [75, 76, 74, 77, 73])
    d = Student('Maksym', 'Vaschenko', 4, [69, 70, 68, 71, 67])
    e = Student('Dima', 'Hohlov', 5, [60, 61, 60, 63, 60])
    f = Student('Yaroslav', 'Dyhanov', 6, [95, 94, 96, 97, 93])
    g = Student('Valerii', 'Albertovich', 7, [100, 100, 100, 100, 100])
    h = Student('Slozno', 'Pridumyvat', 8, [70, 71, 69, 72, 68])
    m = Student('Samuel', 'Smith', 9, [65, 64, 63, 67, 66])
    n = Student('Ded', 'Doed', 10, [61, 74, 82, 64, 60])
    group = Group()
    group.add_student(a)
    group.add_student(b)
    group.add_student(c)
    group.add_student(d)
    group.add_student(e)
    group.add_student(f)
    group.add_student(g)
    group.add_student(h)
    group.add_student(m)
    group.add_student(n)
    print(group)


if __name__ == '__main__':
    main()

