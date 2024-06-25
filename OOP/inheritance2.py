class A:
    def show(self):
        print('Hello A')

    @staticmethod
    def disp():
        print('Welcome A')

class B(A):
    def display(self):
        print('Hello B')

class C(B):
    @staticmethod
    def getMsg():
        print('Hello C')

c = C()
c.disp()
c.display()