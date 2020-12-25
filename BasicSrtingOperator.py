# Basic String Operator like repeating, slicing or connecting
str = "Hello world, This is a string "
print(len(str))  # Get the length
print(str * 3)  # Repeating string as multiply
print(str.replace('Hello', 'Hi'))  # Replacing, Variable and replace method do the replacing
print(str.split(','))  # Split, it looking for separator value and replace with comma, this can create data type
print(str.startswith('H'))  # Starts with
print(str.endswith('H'))  # Ends with, it return bkz it sentence ends with 'g'
print(str.upper())  # Its call a function that return upper class
print(str.lower())  # Its call a function that return lower class
print(str.capitalize())  # Its call a function that return capitalize

# Slicing or Getting a sub String
print(str[0:5])  # Get the first 5 - zero based
print(str[6:])  # Get start with 6 position and by default it will end
print(str[-7:])  # -7 its start from back words
print(str[5:10])  # Find the word of this position
# Index of substrings
l = 'o'
c = str.find(l) # -1 if not found
print(f'Find returned {c}') # If result count as -1 number that simply not there

i = str.index(l)  # Both can find the same index result
print(f'Find returned {i}')
"Hello world, This is a string "
x = str[:i] # position call find to find the string
print(x)
