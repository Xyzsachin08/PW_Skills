class A:
  def add(self, *nums):
    print(sum(nums))

a1 = A()
a1.add(10,20)
a1.add(10,20,30)