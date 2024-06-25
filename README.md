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
## Q.8 Write a program to reverse a string in python.
```python
str = "Hello"
print(str[::-1])
```
## Q.9 How do you determine if a string is a palindrome?
```python
str = "abba"
str1 = str[::-1]

if(str == str1):
    print("Palindrome")
else:
    print("Not a palindrome")
```
## Q.10 How do you calculate the number of numerical digits in a string?
```python
allDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

str = "Hello45"

digits = 0

for i in str:
    if i in allDigits:
        digits += 1
    
print(digits)
```
## Q.11 How do you find the count for the occurrence of a particular character in a string?
```python
str = "Hello"
count = 0

for i in str:
    if i=='l':
        count += 1

print(count)
```
## Q.12 How do you find out if the two given strings are anagrams?
```python
s1 = "Silent"
s2 = "Listen"

s1 = s1.lower()
s2 = s2.lower()

if(sorted(s1) == sorted(s2)):
    print("Anagram")
else:
    print("not anagram")
```
## Q.13 How do you find the non-matching characters in a string?
```python
s1 = "Hello"
s2 = "Hallo"

if(len(s1) != len(s2)):
    print("Strings of different length")
else:  
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print("Character not matched at index", i)
```
## Q.14 How do you calculate the number of vowels and consonants in a string?
```python
str = "Welcome"
str = str.lower()

vowels = 0
consonants = 0

for i in range(len(str)):
    if str[i] in ('a', 'e', 'i', 'o', 'u'):
        vowels += 1
    elif(str[i]>='a' and str[i]<='z'):
        consonants += 1

print(vowels)
print(consonants)
```
## Q.15 How do you total all of the matching integer elements in an array?
```python
arr = [1, 2, 3, 4, 5, 6, 4]
target = 4
sum = 0

# for i in arr:
#     if(i == target):
#         sum = sum + i

for i in range(len(arr)):
    if(arr[i] == target):
        sum = sum + arr[i]

print(sum)
```
