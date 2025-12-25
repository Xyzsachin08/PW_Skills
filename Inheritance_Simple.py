class animal:
    def __init__(self,name):
        self.name = name
        
    def eat(self):
        print(self.name+"Animal is eating")
        
class dog(animal):
    def __init__(self, name,type):
        super().__init__(name)
        self.type = type
        
    def getThenameofdog(self):
        print(self.name)
        print(self.type)
        
d1 = dog("moti","Dobberman")
d1.eat()

d1.getThenameofdog()