"""
A set is an unordered collection data type which is not easy to control, unique which is
not duplicate, immutable which is once data type add we can not change and hash table that mean first
memory access.
Fundamental different between set and list is set much faster but not easy to modify but list can
"""
# Creating a set
s = {1, 2, 3, 3, 4, 5}
print(s)
l = ['Runny', 'Sunny', 43]  # Set determining position,
s = set(l)
print(s)  # Result can see it's unique, immutable and unordered datatype
# Adding items
s.add('Hello')
s.update([1, 2, 3, 'Hello'])
print(s)  # Result can see unordered and unique items only
# Removing Items
s.discard('Hello')  # will not through an error if item is not there
s.remove(1)  # will throw error if item is not there
v = s.pop()  # Pop help to what you want to do bkz still exist in memory
print(s)  # Result generate as found on there
# Can not change items
# s[0] = 'A'  # Error
# print(s[0])
s.remove(3)
s.add(12)
print(s)

x = set('abcd')
y = set('cdefg')

s = x.union(y)  # All the elements that are in either set
print(f'Union:{s}')

s = x.intersection(y)  # All the elements that are in both set
print(f'Intersection:{s}')

s = x.difference(y)  # All the elements that are in both set
print(f'Intersection:{s}')  # All the elements that are in x but not y

s = x.symmetric_difference(y)  # All the elements that are in one of the sets
print(f'Symmetric:{s}') # It will giving back unique order of items

