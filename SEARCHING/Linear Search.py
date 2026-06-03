n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)
print("Your Array is: ",arr)

m = int(input("Enter element to search: "))

for z in range(0,n):
    if arr[z] == m:
        print("Element found at index", z)
        break

else:
    print("Element not found")