# Sets are used to store multiple items in a single variable.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

nums = {1, 2, 3, 4}
print(nums, type(nums))

x = {1, 2, 3, 4, 4}
print(x)   # it does not prints 4 twice , as set does not allow duplicates


# it considers True->1 and False->0
a = {'one', 2, True, 1, False, 0}
print(a)
print(len(a))

# You cannot access items in a set by referring to an index or a key.
# print(nums[0])  

for i in nums:
    print(i)


if 'one' in a:
    print('found')
else:
    print('not found')

print('one' not in a)   #  false
