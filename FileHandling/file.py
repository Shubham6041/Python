f = open('sample.txt', 'a')
# print(f.read())
# print(f.read(11))
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x+'hii')

f.write('writing some content to the file')


f.close()    # It is a good practice to always close the file when you are done with it.


f = open('sample.txt', 'w')
f.write('How are you?')
f.close()


f = open('sample.txt', 'r')
print(f.read())
f.close()

# import os
# os.remove('sample.txt')



