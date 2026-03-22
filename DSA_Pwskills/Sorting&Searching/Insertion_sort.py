arr = [12, 11, 13, 5, 6]

for i in range(1, len(arr)):
    key = arr[i]          # सध्याचा element घ्या
    j = i - 1
    # key योग्य जागेवर insert करा
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]   # मोठा element उजवीकडे सरकवा
        j -= 1
    arr[j + 1] = key

print("Sorted array:", arr)
