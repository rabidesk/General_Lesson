"""
Dictionary is key index value(Set index by key)
which can be any immutable type(mean unchangeable type)
"""
# Crate a dictionary in two ways as seen line 6 and 8
d = {'pet': 'Dog', 'age': 7, 'Name': 'Spot'}
print(d)
d = dict(pet='dog', age=6, name='sport')
print(d)
# Get keys and values
print(f'Items:{d.items()}')  # It returns like items values
print(f'Keys:{d.keys()}')  # It returns everything key value pair
print(f'Values:{d.values()}')  # It returns value without keys value

# How to get value from the key
print(f'Name:{d["name"]}')  # Single quote doesn't support
# print(f'Test:{d["anonymous"]}') # It generate error bkz name is not found
d['trick'] = 'sit'  # It just add the key value as automatically added
print(d)
d['trick'] = 'roll over'  # It just simply change it as added on the list that mean the key itself can not change
print(d)
# Removing an item
del d['trick'] # deleted with key value mean all the associated file is deleted
print(d)
# Testing for existence (Covered in future video)
if 'name' in d: # This if statement tell that if name is there then do something for d
    print(d['name']) # printing method can only run when name is exist in the dictionary
# Looping
for key in d.keys(): # It said that for every key in dictionary key
    print(f'{key}={d[key]}') # Every key in the dictionary key going to printout dictionary value correlates with key




