"""
Tuple is the first list that can not be modified
It's solely to exchange data that typically use between object and classes
"""
# Creating Tuple
d = (1,2,3,4) # Just create a variale 'd'
print(d)
# How to access the elements inside those tuple
print(f'Index:{d[0]}')
print(f'Slice:{d[2]}')
print(f'Boolean:{4 in d}')
# Assignment
(x,y,z) = (1,2,3) # Assignment just to tell take the variable x, y, z and assign to the number
print(x)
print(y)
print(z)

(x,y,z) = range(1,4) # Under the hood python making variable and can sign to the variable using the range function
# It can goes as ranging 1 +3 is 4 as seen from the result
# Range itself not returning the tuple, here the range itself telling that go through loop
print(x)
print(y)
print(z)
print(range(1)) # Range print as 0,3





