
 
    
                         
arr = [24,67,87,23,89,89,76,67]
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if arr[j] < arr[min_index]:
            min_index = i
            arr[j], arr[min_index] = arr[min_index], arr[j]
            
print("sorted array",arr)


 