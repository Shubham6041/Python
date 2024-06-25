# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

student = {
    'name' :'Shubham',
    'age' : 21,
    'x' : [1, 2, 3, 4],
    'fruits' : ('Apple', 'Banana')
}

print(student)
print(type(student))

# we can also declare dictionary using dict constructor
stud = dict(name = 'Shubham', age = 21)
print(stud)
print(type(stud))

print(student['name'])
print(len(student))

print(student.get('age'))

print(student.keys())

print(student.values())
print(student.items())