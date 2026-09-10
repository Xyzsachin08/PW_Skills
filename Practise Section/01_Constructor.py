class Grandfather:
  def __init__(self,name ,age):
    self.name = name
    self.age = age

  def display(self):
    print("Name is ",self.name)
    print("Age is", self.age)



g1 = Grandfather("sachin",85)
g2 = Grandfather("nandini",84)
g3 = Grandfather("nandini",84)
g1.display()
g2.display()
g3.display()