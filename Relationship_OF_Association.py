'''class Teacher:
    def teach(self):
        print("Teacher is teaching.")

class Student:
    def __init__(self, teacher):
        self.teacher = teacher  # student is connected to teacher

    def learn(self):
        self.teacher.teach()  # student asks teacher to teach

t = Teacher()         # create a teacher
s = Student(t)        # give that teacher to student

s.learn()             # student learns from teacher'''



class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching.")

class School:
    def __init__(self, teacher):
        self.teacher = teacher  # Association

    def start_class(self):
        self.teacher.teach()  # Using Teacher class

# Creating a Teacher object
t1 = Teacher("Mr. John")

# Passing Teacher object to School
s1 = School(t1)

s1.start_class()

