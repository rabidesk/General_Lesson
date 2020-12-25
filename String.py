# String in python
for x in 'hello': # For x each letter in the world "Hello"
    print(f'{x} = {ord(x)}') # To print in order numerical value
# How to make a string
first = "Karlos" # Either single or double qoute
last = "Lois"  # Either single or double qoute
print(first + ' ' + last) # Merge them together as concatenate
print(f'Hello my name is {first} {last}') # Tend to use formatted to avoid issues
light = "Light's intensity" # vabriable light hold single and double quote as used how
print(light)
# Under the hood
"""
Sting is a unified code of character that specifically formatted in utf-8 , 
It can be different way to apply search through google
String is a sequence of one or more characters that can also numerical value
"""
p1 = chr(71)
p2 = chr(111)
print(p1 + p2)
print(chr(8710)) # Way beyond ascii as each letter and symbol hold some specific character
# Escape Characters - that start with a slash \
print(f'Hello{chr(13) + chr(10)} world') # Chr(13) for hard return and chr(10) is for line feed for 2 different lines
print(f'Hello\r\nWorld') # \ r this follow return or \n is new line
strTest = "Hello\tWorld"  # Tab inside the characters
print(strTest)
light = 'Light\'s' # Scaping help to find in convenient way to use or which quote you use
print(light)
qoute = "Then he said \"hello\" to me"
print(qoute)

# Errors, that must format strings to avoid
name = "Sunny"
age = 44
# print(name + ' ' + age) This generate error
print(f'My name is {name}, I am {age} years old!') # Expression can be both as next line
print("My name is %s, I am %i years old!" % (name,age)) # %s Name hold the first string and %i is second integer



