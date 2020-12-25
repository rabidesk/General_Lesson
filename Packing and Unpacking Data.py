"""
We can not easily use list set touple set and dictionary as problem found with *arg and **kwarg
Instead we have to pack and unpack data
"""
# How to Packing data
def pack(*nums): # This * mean one or more variables & it say next line print this out.
    print(f'Packed: {nums}')
    for x in nums: # while x in the numbers as listed in for loops as set in the packet
        print(f'Packed:{x}')

pack(1,2,3)
# How to Unpacking data
def unpack(a,b,c): # List it out to define unpacking data which is a, b, c
    print('Unpack') #To know unpacking
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')

num = [1,2,3]
unpack(*num) # This asteric sign tell the python that you are going to be packing and unpacking data, python will
                # take care of all the messy details so I don't have to .
# Dictionary issue
d = dict(name = 'James', age = 33, pet = 'cat')
print('Packing dictionary')
pack(*d)
print('Unpacking dictionary')
unpack(*d)
# Packing Dictionary
def packdict(**nums): # double * asterisk sign for wild character or wildcard.
                      # It also know as **kwarg ( Keyword argument ). Dictionary is nother more than keyword args
    print(f'nums = {nums}')
    print(f'Packeed:{nums}')
    for k in nums:
        print(f'Packed:{k}')
packdict(name='Bones kick', age = 46, pet = 'Cats') # Calling dict functinon that converting dictionary data for us
                                                     # Since it has double ** asterisk that help to access
                                                     # to entire object as a dictionary
# Unpacking a dictionary
def unpackdict(name, age, pet):
    print('Unpacking a dictionary')
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(f'Pet: {pet}')

d = dict(name = 'James', age = 33, pet = 'cat')
unpackdict(**d)  #  double ** asterisk sign tell python that all kinds of data under the hood with
                  # kyword agrs and create a dictionary as unpack line no 39 which is unpackdict (name, age, pet)




