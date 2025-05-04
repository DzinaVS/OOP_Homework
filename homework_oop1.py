class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = float()

    def full_name(self):
        return (self.name + ' ' + self.surname)
    
    def rating_Lectors(self, lector, course, rating):
        if isinstance(lector, Lectors) and course in self.courses_in_progress and course in lector.courses_teach:
            if course in lector.ratings:
                lector.ratings[course] += [rating]
            else:
                lector.ratings[course] = [rating]
        else:
            return 'Ошибка'
        
    def avg_grades(self):
        list_to_int = []
        for val in self.grades.values():
            list_to_int = [int(item) for item in val]
        self.average_grades = sum(list_to_int) / len(list_to_int)
        return self.average_grades  
    
    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания: {round(self.avg_grades(), 1)}" 
                f"\nКурсы, в процессе изучения: {', '.join(self.courses_in_progress)} \n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
    
    def __gt__(self, student):
        return self.avg_grades() > student.avg_grades()
        
    def __lt__(self, student):
        return self.avg_grades() < student.avg_grades()

class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_teach = []

    def full_name(self):
        return (self.name + ' ' + self.surname)

class Lectors(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ratings = {}
        self.average_ratings = float()

    def avg_ratings(self):
        list_to_int = []
        for val in self.ratings.values():
            list_to_int = [int(item) for item in val]
        self.average_ratings = sum(list_to_int) / len(list_to_int)
        return self.average_ratings  
    
    def __gt__(self, lector):
        return self.avg_ratings() > lector.avg_ratings()
    
    def __lt__(self, lector):
        return self.avg_ratings() < lector.avg_ratings()

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(self.avg_ratings(), 1)}"

class Ecsperts(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def marks(self, student, course, grade):
        if isinstance(student, Students) and course in self.courses_teach and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
    
students_list = [] 
course = 'Python'
def students_average_ratings(students_list, course):
    all_grades = 0
    all_students = 0
    for student in students_list:
        if course in student.courses_in_progress:
            all_grades += student.average_grades
            all_students += 1
    return all_grades / all_students


lectors_list = []
def lectors_average_ratings(lectors_list, course):
    all_rating = 0
    all_lectors = 0
    for lector in lectors_list:
        if course in lector.courses_teach:
            all_rating += lector.average_ratings
            all_lectors += 1
    return all_rating / all_lectors

student_1 = Students('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']
students_list += [student_1]

student_2 = Students('Kan', 'Kun', 'man')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Git']
students_list += [student_2]

ecspert_1 = Ecsperts('Some', 'Buddy')
ecspert_1.courses_teach += ['Python']

ecspert_2 = Ecsperts('Mary', 'Kay')
ecspert_2.courses_teach += ['C++']
ecspert_2.courses_teach += ['Python']

lector_1 = Lectors('Bob', 'Smith')
lector_1.courses_teach += ['Python']
lectors_list += [lector_1]

lector_2 = Lectors('Van', 'Damm')
lector_2.courses_teach += ['Python']
lectors_list += [lector_2]

ecspert_1.marks(student_1, 'Python', 10)
ecspert_1.marks(student_2, 'Python', 9)

ecspert_2.marks(student_1, 'Python', 9)
ecspert_2.marks(student_2, 'Python', 8) 


student_1.rating_Lectors(lector_1, 'Python', 6)
student_1.rating_Lectors(lector_2, 'Python', 4)

student_2.rating_Lectors(lector_1, 'Python', 5)
student_2.rating_Lectors(lector_2, 'Python', 9)

print(f'Студенты: \n{student_1} \n \n{student_2}')
print(f'\nСредняя оценка за домашние задания по курсу {course}: {students_average_ratings(students_list, course)}')
print(f'\nЛекторы: \n{lector_1} \n \n{lector_2}')
print(f'\nСредняя оценка за лекции по курсу {course}: {lectors_average_ratings(lectors_list, course)}')
print(f'\nЭксперты: \n{ecspert_1} \n \n{ecspert_2}')

if student_1 > student_2:
    print(f'\n{student_1.full_name()} учится лучше чем {student_2.full_name()}')
elif student_1 < student_2:
    print(f'\n{student_1.full_name()} учится хуже чем {student_2.full_name()}')
else:
    print(f'\n{student_1.full_name()} и {student_2.full_name()} учатся одинаково') 

if lector_1 > lector_2:
    print(f'\n{lector_1.full_name()} преподаёт лучше чем {lector_2.full_name()}')
elif lector_1 < lector_2:
    print(f'\n{lector_1.full_name()} преподаёт хуже чем {lector_2.full_name()}')
else:
    print(f'\n{lector_1.full_name()} и {lector_2.full_name()} преподают одинаково')


        
