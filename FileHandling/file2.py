# f = open('one.txt', 'x)

f = open('one.txt', 'w')
f.write('How are you ?')
f.close()

f = open('one.txt')
print(f.read())
f.close()