# tuple items are immutable.
# if we want to change or modify the tuple then we have to convert it into the list.

nums = (2, 4, 6, 8)
print(type(nums))

x = list(nums)
x.append(9)
print(x, type(x))

x[1] = 3
print(x)

x.insert(0, 1)
print(x)

# unpacking the items of tuple
a, b, c, d = nums
print(a, b, c, d)
print(type(a))      # int


# The number of variables must match the number of values in the tuple, if not, you must use an asterisk to 
# collect the remaining values as a list.
fruits = ('Apple', 'Banana', 'Mango', 'Orange', 'Guava')
x, y, *z = fruits   
print(x, y)
print(z)
print(type(z))

# join tuples
p = nums + fruits
print(p)

q = nums * 2    # it will gives each value doubled
print(q)


# tuple methods
# count
print(fruits.count('Banana'))

print(fruits.index('Guava'))    