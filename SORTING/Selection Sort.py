n = int(input("Enter size of array: "))
arr = []
for i in range(0,n):
    x = int(input("Enter array elements: "))
    arr.append(x)
print(arr)

for i in range(0,n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            k = arr[i]
            arr[i] = arr[j]
            arr[j] = k

print("Sorted array is")
print(arr)

