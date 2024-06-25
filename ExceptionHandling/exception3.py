try:
    try:
        print(x)
    except Exception as e:
        print('yeah , error got', type(e))
    print(10/0)

except ZeroDivisionError as e:
    print('exceptiuon handled', type(e))

finally:
    print('Done with exception handling!!')