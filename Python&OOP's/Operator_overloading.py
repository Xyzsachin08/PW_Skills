'''# Example of operator overloading first normally
print(10*10)

# that's is the example of a operator overloading
print("sachin" "  "*10)'''


'''class num:
    def __init__(self,x):
      self.x = x
      
    def __add__(self,other):
        return self.x + other.x
        
n1 = num(6)
n2 = num(7)
print(n1+n2)'''

class Complexnumber:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,sachin):
        return self.x + sachin.x,self.y + sachin.y
    
n1 = Complexnumber(9,8)
n2 = Complexnumber(5,7)
print(n1+n2)
    



