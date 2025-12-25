arr = [15,23,12,14,45,52,46,41,12,53,56,47,56,23,24,12,12,23,15,16,23,14,10,5,7,9,66,3,25.,56,4]
n =len(arr)
for i in range (n):
    
    for j in range(0,n-1-i):
        if arr[j] > arr[j+1]:
         arr[j], arr[j+1] = arr[j+1], arr[j]
    
    
        
print("Sorted array",arr)


