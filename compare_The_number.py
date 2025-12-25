'''class compare_the_number:
    def sachin(a,b):
        if a > b:
            return a
        else:
            return b
per = compare_the_number
a = 10
b = 20
print(per.sachin(a,b))
c = per.sachin(a,b)
print(c*2)'''



class person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def sachin(self):
        return self.age
per = person("Sachin",90)
print(per.sachin())
            