try:
    print(10/0)

except NameError:
    print('this is name error')
    
except ZeroDivisionError:
    print('this is Zero division error')

except ArithmeticError as e:
    print('this is arithmetic error',e, type(e))

except Exception as e:
    print('exception handled', e, type(e))