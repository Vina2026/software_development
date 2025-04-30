
""""
Neven Said

Lab 11, class in Python, extra points
"""


class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = {}

    def add_grade(self, subject, grade):
        self.grade[subject] = grade

    def get_average_grade(self):
        if not self.grade:
            return 0

        sum = 0

        for x in self.grade:
            sum += self.grade[x]

        return sum / len(self.grade)


student1 = Student("Peter Pan", 20)
student1.add_grade("English", 90)
student1.add_grade("Math", 80)
student1.add_grade("Science", 90)
student1.add_grade("History", 85)


student2 = Student("Ana", 25)
student2.add_grade("English", 80)
student2.add_grade("Math", 75)
student2.add_grade("Science", 90)
student2.add_grade("History", 85)

print(f"\n{student1.name} average grade = {student1.get_average_grade()}\n")

print(f"\n{student2.name} average grade = {student2.get_average_grade()}\n")
