
class One:
    x = 4

p = One()
print(p.x)


# the first parameter of any instance method is always self

class Three:
    def disp(self):
        print('Hello')

q = Three()
q.disp()


class Two:
    def show(self, a, b):
        print(a+b)


r = Two()
r.show(5, 4)

# methods that don't use the self parameter
class Three:
    @staticmethod    # decorator
    def display():
        print('Hello World')


t = Three()
t.display()

