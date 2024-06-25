class A:
    def __init__(self, name):
        self.name = name
        print(name)

    def start(self):
        print('Hello')

class B(A):
    def __init__(self, name, age):
        A.__init__(self, name)    # using class name
        A.start(self)

        super().__init__(name)    # using super() method
        super().start()
        print('construcotr B')

b = B('Om', 22)


