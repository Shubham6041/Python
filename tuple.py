# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

fruits = ('Apple', 'Banana', 'Orange', 'Mango')
print(fruits)
print(type(fruits))

print(fruits[1])
print(fruits[-5:-1])
print(fruits[-4:-1])
print(fruits[-3:-2])


# if we specified single element in the tuple then we have to add ',' 
fruit = ("Banana")
print(type(fruit))    # gives type -> str

fruit1 = ('Banana',)
print(type(fruit1))   # type -> tuple

for i in fruits:
    print(i)

if 'Banana' in fruits:
    print("found")
else:
    print('Not found')