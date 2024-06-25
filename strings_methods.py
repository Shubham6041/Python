x = 'Hello '
num = 4
print(x.upper())
print(x.lower())
print(x.strip())     # it removes white spaces (except the white spaces within string)

# print(x.replace('e', 'a'))

# print("Hello" + num)   # gives the error

#using F-String
txt = f"Hello, {num}"
print(txt)

print(x.capitalize())   # Converts the first character to upper case

print(x.casefold())   # Converts string into lower case

print(x.count('l'))    # Returns the number of times a specified value occurs in a string

print(x.encode())     # Returns an encoded version of the string