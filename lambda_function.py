# syntax -->  lambda arg : expression

x = lambda a : a * 5 
print(x(5))

y = lambda b, c : b * b + c
print(y(3, 4))


#lambda function inside the  function

def show(n):
    x = lambda a : a * n
    print(x(5))

show(5)


def disp(n):
    return lambda a : a + n

x = disp(4)
print(x(2))