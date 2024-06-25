x = {
    'name': 'Om',
    'id' : 11,
    'colors' : ['Red', 'Pink']
}

# Print all key names in the dictionary, one by one:
for i in x:
    print(i)

# Print all values in the dictionary, one by one:
for i in x:
    print(x[i])

for i in x.values():
    print(i)

for i in x.keys():
    print(i)

for i, j in x.items():
    print(i, j)

# copy the dictionry -> two methods
y = x.copy()
print(y)
print(type(y))

z = dict(x)
print(z)