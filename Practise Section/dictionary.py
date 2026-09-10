Dict1 = {1: "sachin", "nandini": "sachin", 3: "nachin"}
print(id(Dict1))
Dict1[4] = "borude"
print(Dict1)
print(id(Dict1))

Dict2 = {4: "sachin", 5: "borude"}
Dict1.update(Dict2)
print(Dict1)



