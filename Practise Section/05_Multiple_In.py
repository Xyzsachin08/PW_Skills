class Father_1:
  def __init__(self, name):
    self.name = name

class Father_2:
  def __init__(self, age):
    self.age = age

class Child(Father_1, Father_2):
  def __init__(self, name, age, occupation):
    Father_1.__init__(self, name)
    Father_2.__init__(self, age)
    self.occupation = occupation

  def display(self):
      print("The name is" , self.name, "The age is", self.age ,"and occupation is", self.occupation)

c1 = Child("sachin",21,"Software Developer")
c1.display()