# once set is created we can't change its items, but we can add new items.

x = {1, 2, 3, 4}
x.add(5)
print(x)

y = {'a', 'b', 'c'}

# To add items from another set into the current set, use the update() method.
x.update(y)
print(x)

# we can also add list, tuple into the set.
lst = ['one', 'two']
x.update(lst)
print(x)

tple = ('Apple', 'Banana')
x.update(tple)
print(x)

# To remove an item in a set, use the remove(), or the discard() method.

x.remove('one')
print(x)

x.discard('Apple')
print(x)

# The clear() method empties the set:
x.clear()
print(x)

# The del keyword will delete the set completely:
del x
# print(x)