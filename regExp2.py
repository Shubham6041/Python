import re

text = 'Hello, My name is ABC'
a = re.search('name', text)
print(a)

b = re.split('\s', text)
print(b)

c = re.split('\s', text, 1)
print(c)

d = re.split('\s', text, 2)
print(d)

e = re.sub('\s', '4', text)
print(e)

f = re.sub('ABC', 'XYZ', text)
print(f)