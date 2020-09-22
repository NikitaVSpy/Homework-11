class Student():

    def __init__(self, number_in_list, name):
        self.number_in_list = number_in_list
        self.name = name

    # def __str__(self):
    #     return f'Имя студента под номером {self.number_in_list}: {self.name}'


class School():
    def __init__(self, students, marks):
        self.students = students
        self.marks = marks

    def __len__(self):
        return len(self.marks)

    def __getitem__(self, i):
        return f'Имя студента под номером {self.students[i].number_in_list}: {self.students[i].name}. Его оценка - {self.marks[i]}'

    def __setitem__(self, key, value):
        self.marks[key] = value

    def __iter__(self):
        for i in range(len(self.marks)): yield self.students[i].name, self.marks[i]


class Activity():
    def __init__(self, st_information, certificate):
        self.st_information = st_information
        self.certificate = certificate

    def __add__(self, other):
        return self.certificate + other.certificate

    def __str__(self):
        return f'Имя студента: {self.st_information.students.name}. Количество его сертификатов - {self.certificate}'

    def __gt__(self, other):
        return self.certificate > other.certificate

    def __ge__(self, other):
        return self.certificate >= other

    def __int__(self):
        return int(self.st_information.marks)

    def __eq__(self, other):
        return self.certificate == other.certificate


if __name__ == '__main__':
    students = [Student(1, 'Василий'), Student(2, 'Иван'), Student(3, 'Олег')]
    mark = ['5', '4', '3']
    s = School(students, mark)

    print('Количество студентов:', len(s))
    print()
    print(s[0])
    print('А теперь ...')
    s[0] = '2'
    print(s[0])

    print()
    for st, m in iter(s):
        print(st, m)

    print()
    st_1 = Activity(School(Student(1, 'Мария'), '5'), 2)
    st_2 = Activity(School(Student(2, 'Наталья'), '4'), 8)
    st_3 = Activity(School(Student(3, 'Марина'), '4'), 8)
    print(st_1, st_2, st_3, sep='\n')

    print('Количество сертификатов на команду:', st_1 + st_2)
    if st_1 > st_2:
        print('У первого студента сертификатов больше, чем у второго')
    else:
        print('У второго студента сертификатов больше, чем у первого')

    print()
    print('Первый студент имеет сертификатов не менее, чем среднее значение по команде?', st_1 >= 5)
    print('Второй студент имеет сертификатов не менее, чем среднее значение по команде?', st_2 >= 5)

    print()
    print('Средняя оценка по команде:', (int(st_1)+int(st_2))/2)

    print()
    print('У второго и третьего студента равное количество сертификатов?', st_2 == st_3)












