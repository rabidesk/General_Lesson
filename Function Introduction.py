"""
Function is block of code that can only run when it's called. It's another fundamental building block of programming
Function return result as data. What is different in parameters and arguments
Function parameters are the name as listed in the function's definition
Function arguments are the real values passed to the function
Parameter are initialized to the values of the arguments supplied
"""


# Define function
def test():  # def keyword mean define with test parenthesis with no parameter
    print('This is function')  # Most IDE indent do automatically


# Define a function with parameters and return a value
def sqft(w, h):  # Take the square feet as parameter for width (w) and height (h)
    v = w * h # Define the some sort of logic as demand you need it and get the result
    return v  # It's return a value, sometime it's not mandatory


# How to call a function
test()  # Since there is no parameter, so don't have to supply any arguments from line 9
# Call a function multiple times
for x in range(5):  # Create a loop in lower boundary 0 (as hidden) and upper boundary 5 and all function test()
    test()  # You can define the block of code and call when need to run
# Call a function with parameters
x = sqft(33, 8)  # The number inside the bracket call arguments but line 16 inside brackets is parameters
print(f'The square footage is {x}')  # Print the result after calling the function
