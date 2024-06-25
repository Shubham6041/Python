
class A:
    name = 'A'
    @staticmethod
    def show():
        print('Welcome A')

    
class B(A):
    @staticmethod
    def display():
        print('Hello B')

b = B()
b.show()