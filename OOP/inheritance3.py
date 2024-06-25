# multiple inheritance

class A:
    name = 'A'
    @staticmethod
    def show():
        print('Hello A')
    
class B:
    @staticmethod
    def display():
        print('Hello B')

class C(A, B):
    @staticmethod
    def getMsg():
        print('Hello C')

c = C()
c.show()
c.display()
c.getMsg()