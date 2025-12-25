'''class Animal :
    def eat(self):
        print("Animal is Eating")
    
class Dog:
    def eat(self):
        print("Dog is Eating")
        
class Cat:
    def eat(self):
        print("Cat is eating")
        
a = Animal()
d = Dog()
c = Cat()

a.eat()
d.eat()
c.eat()'''


#Duck typing

'''class Dog:
    def Oradto(self):
        print("Bark")

class Cat:
    def Oradto(self):
        print("Meow")
        
class Tiger:
    def Oradto(self):
        print("Darkali")

def animal_sound(sachin):
   # sachin.speak()
    sachin.Oradto()

d = Dog()
c = Cat()
t = Tiger()

animal_sound(d)   # Output: Bark
animal_sound(c) 
animal_sound(t)   # Output: Meow'''


# oprrator overloading

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)   # Output: 300

#Method overriding (inheritance)

class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

a = Animal()
d = Dog()
c = Cat()

a.speak()  # Some sound
d.speak()  # Bark
c.speak()  # Meow

