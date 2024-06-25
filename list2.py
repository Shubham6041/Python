lst = [2, 4, 6, 8]

# copy the list into another list
lst1 = lst.copy()
print(lst1)

lst2 = list(lst)
print(lst2)

# join the lists
lst3 = ['one', 'two']
lst4 = lst3 + lst
print(lst4)

lst3.extend(lst)
print(lst3)