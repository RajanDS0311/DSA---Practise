n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)
print("Your Array is: ",arr)

for i in range(0,n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            k = arr[i]
            arr[i] = arr[j]
            arr[j] = k
print("Your Sorted Array is: ",arr)

m = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == m:
        print("Element found at index", mid)
        break

    elif m < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

else:
    print("Element not found")






