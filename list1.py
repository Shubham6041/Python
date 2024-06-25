lst = [2, "one", "two", 3]
lst[1] = 'Hey'

print(lst)

lst[0:2] = [1, 2]
print(lst)

lst.insert(2, 'one')
print(lst)

lst.append(4)
print(lst)

# three methods -> remove an element from the list
lst.remove('two')
print(lst)

lst.pop(1)
print(lst)

del lst[1]
print(lst)

# empty the list
lst.clear()
print(lst)