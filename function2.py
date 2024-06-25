# arbitrary arguments
# If we do not know how many arguments that will be passed into your function, add a * before the parameter name in 
# the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly

def show(*num):
    print(num[1])    

show(2, 4, 6)

# Keyword Arguments (kwargs)
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter

def show1(a, b, c):
    print(a)

show1(a = 5, b = 7, c = 3)

# arbitrary Keyword Arguments (kwargs)
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly

def disp(**x):
    print(x['y'])

disp(x = 'Hii', y = 'Hello')


# Default Parameter Value
# if we call the function without argument, then it uses the default value

def display(name = 'Shiv'):
    print('My name is '+name)

display('Om')
display()
