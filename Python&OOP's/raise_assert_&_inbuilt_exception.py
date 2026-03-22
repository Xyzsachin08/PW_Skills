'''arr = [1,2,3]
if len(arr) <4:
    raise Exception(f'Length of the given list is {len(arr)} which is <4')


def cube_root(num):
    #check if the num is positive and if not, I would raise an exception
    if(num <0):
       assert (num >=0), "pass a positive number"
    return num**(1/3)



print(cube_root(8))

try :
    val = cube_root(-8)
    print(val)
    
except :
    print("Please provide valid positive integer for the cube root")
    
    print("Last line")

print(cube_root(-8))

print("Last line")'''


'''def operate(num):
    try :
        result = 5/num
    except ZeroDivisionError :
        print("cant't divide a number by 0")
        
    else:
        print(result)
        
operate(0)'''


def operate(num):
    try :
        result = 5/num
    except ZeroDivisionError :
        print("cant't divide a number by 0")
        
    finally:
        print("This portion of the code will always be executed")
        
operate(0)