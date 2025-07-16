n=int(input("enter no. of elements"))
arr=[]
for i in range(n):
   x=int(input("enter element"))
   arr.append(x)
for item in arr:
   print(item,end=' ')
print()

Q1

arr = [10, 20, 30, 40]
print("enter array elements")
for item in arr:
    print(item, end=' ')
print()
print("The individual elements are:")
print("Element at index 0:", arr[0])
print("Element at index 1:", arr[1])
print("Element at index 2:", arr[2])
print("Element at index 3:", arr[3])

Q2

arr = [10, 20, 30, 40]
n=int(input("enter an element to be added in the end of the array:"))
arr.append(n)
print("new array:")
for item in arr:
    print(item, end=' ')
print()

Q3

arr = [10, 20, 30, 40]
print("Original array:")
for item in arr:
    print(item, end=' ')
print("After reversal:")
n = len(arr)
for i in range(n // 2):
    temp = arr[i]
    arr[i] = arr[n - i - 1]
    arr[n - i - 1] = temp
for item in arr:
    print(item, end=' ')
print()

Q4
arr = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Enter the number to count: "))
count = 0
for i in arr:
    if i == x:
        count += 1
print(f"{x} appears {count} times in the array.")