#Public 
class Student:
    def __init__(self, name):
        self.name = name  # public variable

    def display(self):  # public method
        print("Name:", self.name)

s = Student("Rahul")
print(s.name)       # ✅ Can access directly
s.display()         # ✅ Can call directly

#Private
class Student:
    def __init__(self, name):
        self.__name = name  # private variable

    def __display(self):    # private method
        print("Name:", self.__name)

s = Student("Sneha")
# print(s.__name)        ❌ Error: can't access directly
# s.__display()          ❌ Error: can't call directly

# ✅ Correct way (not recommended)
print(s._Student__name)     # Output: Sneha

#Protected
class Student:
    def __init__(self, name):
        self._name = name  # protected variable

    def _display(self):    # protected method
        print("Name:", self._name)

s = Student("Ravi")
print(s._name)        # ⚠️ Allowed, but not recommended
s._display()          # ⚠️ Allowed, but not recommended
