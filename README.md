## Q.1 Write a program to reverse the number.
```python
n = int(input("Enter the number: "))
reverse = 0
while(n>0):
    digit = n % 10
    reverse = reverse*10 + digit
    n = n // 10
    
print(reverse)
```
