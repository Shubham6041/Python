# it is same as the toString() method in java
# used to return the string representation of an object.


# without __str__() function

class One:
    def __init__(self, name, age):
        self.name = name
        self.age = age

o = One('Shiv', 11)
print(o)

# with the __str__() function
class Two:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} : {self.age}"
    
p = Two('Om', 21)
print(p)