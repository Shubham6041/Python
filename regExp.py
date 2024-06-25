import re

text = 'Hello, M0y name is X1YZ'
x = re.search('^Hello.*XYZ$', text)

if x:
    print('yes')
else:
    print('no')

y = re.findall('[a-m]',text)
print(y)

a = re.findall('He.{2}o', text)
print(a)

b = re.findall('He..o', text)
print(b)

c = re.findall('H.*o', text)
print(c)

d = re.findall('n.?m', text)
print(d)

e = re.findall('n.+m', text)
print(e)

f = re.findall('name|game', text)
print(f)

g = re.findall('[eo]', text)
print(g)

h = re.findall('[^eo]', text)
print(h)

i = re.findall('[10]', text)
print(i)

str1 = 'He is 50 and she is 41'

j =re.findall('[0-5][0-8]', str1)
print(j)

