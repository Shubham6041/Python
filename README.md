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
## Q.3 Write a program to print fibonacci series.
```python
n1 = 0
n2 = 1

for i in range(10):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
```
## Q.4 Write a program for prime number.
```python
def prime(n):
    if(n == 0 or n == 1):
        return False
        
    if(n == 2):
        return True
        
    for i in range(2, n//2 +1):
        if(n%i == 0):
            return False
            
    return True

num = 21
print(prime(num))
```
## Q.5 Write a program for finding the leap year.
```python
year = 2016

if(year%400 == 0 and year%100 == 0):
    print("leap year")
elif(year%4 == 0 and year%100 != 0):
    print("leap year")
else:
    print("not a leap year")
```
## Q.6 Write a program for calculating the factorial of the number.
```python
num = 5
fact = 1

if(num<0):
    print("can't calculate the factorial of negative number")
elif(num == 0):
    print(1)
else:
    for i in range(1, num+1):
        fact = fact * i
        
    print(fact)
```
## Q.7 Write a program to reverse the array(list).
```python
arr = [1, 2, 3, 4, 5]
# arr.reverse()
# print(arr)

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = ' ')
```

