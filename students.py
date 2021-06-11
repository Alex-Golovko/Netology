class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and self.courses_in_progress and self.finished_courses and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.grades < other.grades


    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {str(self.grades)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.grades < other.grades

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {str(self.grades)}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in lecturer.courses_attached and course in student.courses_in_progress and grades <= 10:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


student = Student('Ruoy', 'Eman', 'man')
student_1 = Student('Alex', 'Golovko', 'man')
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Some', 'Buddy')

student.rate_lecturer(lecturer, 'Python', 10)
student_1.rate_lecturer(lecturer, 'Python', 10)




reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student_1, 'Python', 10)


print(lecturer)
print()
print(student)
print()
print(student_1)
print()
print(reviewer)
