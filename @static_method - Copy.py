#code 1
class Result:
    @staticmethod
    def is_pass(marks):
        return marks >= 35

# वापर:
print(Result.is_pass(40))  # Output: True
print(Result.is_pass(25))  # Output: False


#code 2
class MathHelper:
    @staticmethod
    def add(x, y):
        return x + y

# वापर:
print(MathHelper.add(10, 5))  # Output: 15

