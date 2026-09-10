class Grandfather:
    def __init__(self, name):
        self.name = name


class Father_1(Grandfather):
    def father1(self):
        print("Father 1")


class Father_2(Grandfather):
    def father2(self):
        print("Father 2")


class Child(Father_1, Father_2):
    def __init__(self, name, age):
        Grandfather.__init__(self, name)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


c1 = Child("Sachin", 21)

c1.display()
c1.father1()
c1.father2()