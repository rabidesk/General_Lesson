# For loop and range
# For loop on lists, tuples, sets
l = [1, 2, 3, 4]  # List
t = (1, 2, 3, 4)  # Tuple
s = {1, 2, 3, 4}  # set

for i in s:  # something like while loop and we are creating a variable in statement itself
    print(f'i = {i}')  # Base on the x value it can run only for i
x = dict(Hena=45, Tamy=44, Heala=33, Cheri=22)  # Simple crate dictionary
print(x)
# Any method can do as you like
for k in x.keys():  # It say each one of those get the value
    print(f'Keys: {k}= {x[k]} ')  # The first k mean the name and second k mean the actual value as set
for k, v in x.items():  # Call the items function to get the all value from the dictionary
    print(f'Items: {k}= {v}')  # K is item name and v is value




