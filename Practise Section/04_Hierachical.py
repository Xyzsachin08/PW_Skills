class Father:
  def __init__(self, name):
    self.name = name

class Child_1(Father):
  def __init__(self, name, age):
    super().__init__(name)
    self.age = age

  def display(self):
    print("The name is", self.name, "and age is", self.age)

class Child_2(Father):
  def __init__(self, name, occupation):
    super().__init__(name)
    self.occupation = occupation

  def display(self):
      print("The name is" , self.name, "and occupation is", self.occupation)

c1 = Child_1("sachin",21)
c1.display()

c2 = Child_2("sachin","software developer")
c2.display()
