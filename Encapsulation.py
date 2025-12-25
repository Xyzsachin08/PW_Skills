class person:
    
    def __init__(self,name,car):
        self.__name = name
        self.__car = car
        
    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name = name
    
    def getcar(self):
        return self.__car
    
    def setcar(self,car):
        self.__car = car
    
per = person("Sachin","Thar")
print(per.getname())
per.setname("Sachin popat Borude")
print(per.getname())
    
        