## Q.1 Write a program to reverse the number.
```python
n = int(input("Enter the number: "))
reverse = 0
while(n>0):
    digit = n % 10
    reverse = reverse*10 + digit
    n = n // 10
    
print(reverse)

# input : 357
# output : 753
```
## Q.2 Write a program for linear search for searching element in a list.
```python
def linearSearch(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    
    return -1

arr = [1, 2, 3, 4, 5, 6]
target = 5

print(linearSearch(arr, target))
```
