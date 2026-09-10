#Split
from ntpath import join


s = "sachin borude, sachin , sachin"
print(s)
b = "borude sachin"
p = s+ " " +b     # string concatination
print(p)



print(s[2])   #indexing
print(s.split())  # split string

print(" ",join(s))  # join need package


print(" onkar \n borude") #string escape
print("onkar \t borude")   #string escape




nan = " hello saburi how are you, are you fine?, tell me about your self "   # replac string
print(nan.replace("are you fine?", "are you happy"))
