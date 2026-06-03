n = int(input("Enter size of array: "))
arr = []
for i in range(0,n):
    x = int(input("Enter array elements: "))
    arr.append(x)
print(arr)

for i in range(1,n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key

print("Sorted array is")
print(arr)