class One:
    __num = 15   # we use '__' to make attributes and methods private

    def show(self):
        print(self.__num)

    def __display(self):
        print('Hello')

a = One()
# we can not acced private attributes out side the class
# print(a.__num)    

# but we can use private attributes inside the class
a.show()

# gives an error
# a.__display()