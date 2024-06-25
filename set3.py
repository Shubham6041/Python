# to join the sets we can use union() method or '|' operator

a = {1, 2, 3, 4}
b = {'one', 'two', 'three', 'four'}

c = a.union(b)
print(c)

d = a | b 
print(d)

# we can join multiple sets

e = {'a', 'e'}
f = {7, 8, 9}

g = a.union(b, e, f)
print(g)

h = a | b | e| f
print(h)

# The intersection() or '&' method will return a new set, that only contains the items that are present in both sets.

var = c.intersection(b)
print(var)

var1 = c & b
print(var1)

# The difference() or '-' method will return a new set that will contain only the items from the first set that are 
# not present in the other set.
x = c.difference(b)
print(x)

y = c - b
print(y)