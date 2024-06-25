lst = [1, 2, 3, 4]
print(lst)
print(type(lst))

lst1 = [2, 'one', 'two', 5]
print(lst1)

for i in lst1:
    print(i)

lst2 = list((2, 4, 6, 8))
print(lst2)

print(lst1[1])
print(lst1[-1])
print(lst2[1:3])

if "one" in lst1:
    print("found")
else:
    print("not found")