class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print("Student name: {self.name}\nStudent age: {self.age}\nStudent grade: {self.grades}")

grades = [student.age for student in student]
print('Average Age Is: {}'.format(sum(grades)/len(grades))