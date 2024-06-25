
x = {
    'name' : 'Om',
    'id' : 11,
    'colors' : ['red', 'pink']
}

# changing the dictionary items.
x['name'] = 'Shiv'
print(x)

x.update({'name' : 'Ganesh'})
print(x)

# adding the items in dictionary.
x['year'] = 2024
print(x)

x.update({'value' : 1})
print(x)

# The pop() method removes the item with the specified key name:
x.pop('value')
print(x)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
x.popitem()
print(x)

# The del keyword removes the item with the specified key name:
del x['colors']
print(x)

# The clear() method empties the dictionary:
x.clear()
print(x)

# The del keyword can also delete the dictionary completely:
del x
