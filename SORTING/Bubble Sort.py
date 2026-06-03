n = int(input("Enter size of array: "))
arr = []
for i in range(0,n):
    x = int(input("Enter array elements: "))
    arr.append(x)
print(arr)

for i in range(0,n):
    for j in range(0,n-1):
        if arr[j] > arr[j+1]:
            k = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = k

print("Sorted array is")
print(arr)

