class Student:
    school_name = "ZP School"

    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("नाव:", self.name)
        print("शाळेचं नाव:", Student.school_name)

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

# Student class चे दोन विद्यार्थी
s1 = Student("Ravi")
s2 = Student("Sneha")

# आधीची माहिती
print("शुरुवातीला:")
s1.show_details()
s2.show_details()

# आता आपण class method ने शाळेचं नाव बदलूया
Student.change_school("New English School")

# बदलल्यानंतर माहिती
print("\nबदलल्यानंतर:")
s1.show_details()
s2.show_details()
