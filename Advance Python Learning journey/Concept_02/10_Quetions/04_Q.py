#Find sum of first n numnbers

n = int(input("Enter a number"))

sum = 0
series = ""

for i in range(1, n+1):
    sum +=i
    series += str(i)
    
    if i !=n:
        series += "+"
    
print(series, "=" , sum)



