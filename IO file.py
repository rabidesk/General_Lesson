"""String in python
String is a unified code of character that specifically formatted in utf-8.
If you want search through google can also apply
Sting also a sequence of one or more character that can also numerical form"""

# for x in 'hello world':
#     print(f'{x}={ord(x)}')
# # How to make a string
# first = "Karlos"
# last = "lois"
# print(f"Hello, my name is {first} {last}")
# light = 'Lights intensity'
# print(light)
#
# p1 = chr(80)
# p2 = chr(100)
# print(p1 + p2)
# Escape characters that start with a slash \
# print(f'Hello{chr(10) + chr(12)} World') # Char (10) for hard return and chr(12) is for line feed for 2 different lines
# print(f'Hello\r\nworld') # This result is return form as new line
# srtTest = "Hello\tworld" # Tab function
# print(srtTest)
#
# name = "Sunny"
# age = 44

# person name and age in between single sentence
# print(f'My name is {name}, I am {age} years old!')
# print("My name is %s, I am %i years old!" %(name, age)) # %s Name hold the first name and %i is hold the second value
#
# str = "Hello World. This is a Planet."
# print(len(str)) # Get the length of sentence
# print(str*3) # Repeating string as multiply
# print(str.replace('Hello', 'Hi'))  # Replace the word in single sentence
# print(str.split('s')) # Split , it looking for separator value as set on there
# print(str.startswith('H')) # It's start with H so the result will be true
# print(str.endswith('a')) # It return false
# print(str.upper()) # Upper case letter
# print(str.lower()) # Lower case letter
# print(str.capitalize()) # Capitalized function
# print(str[0:5]) # Get the first 5 - zero based letter
# print(str[6:]) # Get start with 6 position and by default it will end
# print(str[-7:]) # It start with from last position
# print(str[5:10])
# # Index of substring
# d = 'W' # create variable d
# c = str.find(d)
# print(f'Find the positioning value as list ={c}')
# i = str.index(d) # Position call find the string
# print(f'Find positioning value as index = {i}')

# How create list and add items to the list and insert items to the position of the list
x = ['James', 'Mark', 40, 'dogs'] # Create x list
print(f'List items:{x}')
print(f'Length of the list is :{len(x)}')
# Index and positioning
print(f'First items:{x[3]}')
print(f'Slice:{x[1:2]}')
x.append('Barger')
x.append('Gombak')
x.insert(2,'Cats')
print(f'New list:{x}') # Print the list of the name added in this program
y = ['Duck','Dog','Birds'] # New items list
x.extend(y)
print(f'After extend list: {x}')
x.remove(40)
print(f'After removing the list of items:{x}')
x.remove('Cats')
print(f'After extend list: {x}')
x.reverse()
print(f'After Revers:{x}')
y = x.copy() # Copies the elements into a new list
y.reverse() # First it change the reverse position
y.append('Apple') # Add new names fruits
print(f'Original list:{x}')
print(f'New list : {y}')
# Delete the whole things
# Clearing all the value that you insert in the list
x.clear()
print(f'After clearing the list:{x}') # Know the list of the items after clearing
print(f'Length of the list is : {len(x)}') # Know the lenght of the code


