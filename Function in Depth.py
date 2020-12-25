# Function insite of function
def test():
    print('Normal Function')
print('\r\n-------No arguments')
test() # Just calling function as expected
# Positional and Keyword Arguments
def message(name,msg,age):
    print(f'Hello {name}, {msg}, You are {age} years old')
print('\r\n==== Positional and Keyword Arguments')
message('James', 'Good morning', 33) # Positional
message('James', 33,'Good morning') # Wrong Positional
message(msg='Good morning', age=45, name= 'James') # Keywords as parameter arguments
message('James', age=45, msg='Good Morning') # Keywords as parameter arguments result will be same though change
# Internal Functions
def counter():
    def display(count=0): # Function in a function
        print(f'Internal:{count}')
    for x in range(5): display(x)
print('\r\n-------Internal Function')
counter()
# *Arguments - Positional variable length arguments
def multiple(*args):  # Going to feed the branch of arguments based on position
    z = 1  # Initialized the value of z
    for num in args: # For the number arguments will be print that
        print(f'Num={num}')  # Going to print the number
        z *=num # Number is multiple by the number with z
    print(f'Multiply : {z}') # Print the value of z after multiply
print('\r\n------*arguments') # see the output
multiple(2,3,1,2,5) # Multiple all the value of order
# ** Kwargs (Keywords arguments) is used to pass a keyword, variable length arguments
# the double star ** is complex
def profile(**person): # Person is a branch of data that going to figure out what to do as seen in line 43,44,45
                     # Bkz its hold all the positional arguments even though several positional arg in same line
                     # The key word arg don't tell how many argument is there.
                     # argument person hold many data as can be figure out and hold double ** singe
    print(person)
    def display(k): # Use this as internal function
        if k in person.keys():print(f'{k} = {person[k]}') # if k value in person.keys then print function call
                                                       # it known as little internal function
        # Since, if is mention so, don't have to worry not define in the line profile
    display('name') # give the keyword name
    display('age') # give the keyword name
    display('pet') # give the keyword name
    display('Food')  # give the keyword name
# Since, keyword K in the keys then
print('\r\n------*Kwargs')
profile(name = 'James', age = 88)
profile(name = 'James', age = 88, pet = 'Cat')
profile(name = 'James', age = 88, pet = 'Cat', food = 'Pizza') # food add but program doesn't
                                                               # crash bkz it not in line no 34
                                                               # Keyword argument is not position in there
                                                               # Position simply doesn't matter
# Lambda functions ( Anonymous functions ) . let create normal one
print('\r\n ======= Lambda') # Add simple deliminator here to see the output configure
def makesqft(width = 0, height = 0): # Define making the sqft for width and height
    return  width * height # calculation will be return
print(makesqft(width=10, height=8)) # value will be return based on multiply
print(makesqft(15,6))  # value will be return based on multiply
# Lambda creation based on anonymous function
# z = lambda x: x * y
sqft = lambda width = 0, height = 0: width * height # lambda is going to replace all of the value
                                                    # of width and height from line no 54
                                                    # Then lambda in line 58 specifically seen them as highlight on
                                                    # the screen and the code for this width and height
print(makesqft(width= 10, height=8))
print(makesqft(15,6))     # it's very shortcut method for as result is same as lambda is very powerful & useful








