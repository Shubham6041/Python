# passing a list as an argument

def get(name):
    print(name[0])

fruits = 'Apple', 'Banana', 'Mango'
get(fruits)

# printing the list using for loop
def show(val):
    for i in val:
        print(i)

show(fruits)

# return values
def disp(x):
    return x*x

print(disp(4))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# put in the pass statement to avoid getting an error.

def func():
    pass

