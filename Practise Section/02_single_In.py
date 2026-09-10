class Grandfather:
  def __init__(self,name ,age):
    self.name = name
    self.age = age

class Father(Grandfather):
  def __init__(self ,name, age ,wife_name):
    super().__init__(name, age)
    self.wife_name = wife_name

  def display(self):
    print("Name is ",self.name)
    print("Age is", self.age)
    print("Wife name is", self.wife_name)

g1 = Father("sachin",85, "teju")
g2 = Father("nandini",84, "teju")
g3 = Father("nandini",84,"teju")
g1.display()
g2.display()
g3.display()