'''
#Higher order funtion:- use the function inside the another function that is call higher order funtion.




#example of higher order function
def greet(greet):
    greet()
    
def display():
    print("Hello Onkar")
    
greet(display)


#Map() - apply to all
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x : x*2,nums)))



#Filter() - Use to filter value 
- only keep the true value

l1 = [85, 50, 64, 75, 35, 25, 15]
print(list(filter(lambda x : x < 50, l1)))





#Reduce = Combine Everything into the one

from functools import reduce
sach = [1, 2, 3]
print(reduce(lambda x,y : x +y, sach))  '''


