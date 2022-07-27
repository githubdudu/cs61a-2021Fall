"""
>>> callahan = Professor("Callahan")
>>> elle = Student("Elle", callahan)
Added Elle
>>> elle.visit_office_hours(callahan)
Thanks, Callahan
>>> elle.visit_office_hours(Professor("Paulette"))
Thanks, Paulette
>>> elle.understanding
2
>>> [name for name in callahan.students]
['Elle']
>>> x = Student("Vivian", Professor("Stromwell")).name
Added Vivian
>>> x
'Vivian'
>>> [name for name in callahan.students]
['Elle']
>>> elle.max_slip_days
3
>>> callahan.grant_more_slip_days(elle, 7)
>>> elle.max_slip_days
7
>>> Student.max_slip_days
3
"""


class Student:
    max_slip_days = 3 # this is a class variable

    def __init__(self, name, staff):
        self.name = name # this is an instance variable
        self.understanding = 0
        staff.add_student(self)
        print("Added", self.name)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

    def grant_more_slip_days(self, student, days):
        student.max_slip_days = days