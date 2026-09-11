class A:
    def add(self, a, b, c):
        print(a+b+c)
        
class B(A):
    def add(self, a, b, c):
        print(a+b+c)
        
a1 = A()
b1 = B()
a1.add(10,20,30)
b1.add(100,0,0)