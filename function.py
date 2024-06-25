# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def func():
    print("Hello World")

func()

def show(name):
    print('My name is '+name)

show('Uday')
show('Sanket')


def display(name, age):
    print('My name is '+name+' and I am '+str(age)+' years old.')

display('Om', 20)
display('Sagar', 22)