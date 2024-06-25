# exception handling --> when an error or exception occurs , python will stop and generate error message
# try and except block is used

try:
    print(10/0)

except:
    print('exception occurs')

finally:
    print('this block will always execute')
