# A dictionary can contain dictionaries, this is called nested dictionaries.

x = {
    'student1' :{
        'name' : 'Yash',
        'id' : 11
    },

    'student2':{
        'name' : 'Pranav',
        'id' : 12
    }

}

print(x)

# we can add dictionaries into the new dictionary.
a ={
    'color' : 'Red',
    'val' : 1
}

b = {
    'color' : 'Yellow',
    'val' : 2
}

c = {
    'a' : a,
    'b' : b
}

print(c)

# access an item from the nested dictionary.
print(x['student1']['name'])