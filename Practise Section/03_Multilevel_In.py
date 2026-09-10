class Grandfather:
  def __init__(self, name):
    self.name = name

class Father(Grandfather):
  def __init__(self, name, age):
    super().__init__(name)
    self.age = age

class Child(Father):
  def __init__(self, name, age, occupation):
    super().__init__(name, age)
    self.occupation = occupation

  def display(self):
      print("The name is" , self.name, "age is", self.age, "occupation is", self.occupation)

c1 = Child("sachin",21,"Softwaredeveloper")
c1.display()
