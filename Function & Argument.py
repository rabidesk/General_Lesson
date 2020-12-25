# Function and arguments
# Function in an arguments
# def test(name, age, pet):
#     print(f'Name: {name}')
#     print(f'Age: {age}')
#     print(f'Pet: {pet}')
#
# def getData():   # One function return data & another function does something with data
#     return dict(name = 'James', age = 33, pet = 'Cat')
# d = getData() # Standalone the data to feed as dictionary
# test(d['name'],d['age'],d['pet']) # This way or the following line super way to call test(**getData())
# test(**getData()) # Easier way to packing data and unpacking data as double ** sing is integrated with getData()
#
# # Function as an Argument
# def funny(data): # We just variable call data, like function take the variable
#     d = data() # data name is not a matter but the matter is call the function , like take variable like treat it like function
#     print(f'Dictionary :{d}') # Use the variable as a function
#     print(f'Name:{d["name"]}')
#     print(f'Age:{d["age"]}')
#     print(f'Pet:{d["pet"]}')
# funny(getData) # Not calling the function, just passing it by only mention (getData) from line 8, That mean funny as the function
#                # Converting (getdata) for function as an argument
# Global Keyword allows code to modify a variable
# Outside of the current scope
x = 1
def test(): # when you define a function actually defining scope, here
            # Global keyword allowed us to do global scope
    x = 7      # Here we define a function which has won scope
    print(x)
test()
print(x)

# Global variable
counter = 0 # Without tab/space put on the fist line counter is consider to be global scope
# Scope issue
def count(max):
    # Without global, python is confused
    global counter # Use the global variable called counter if not then it will error, global keyword help to run
                   # global keyword help to run the program
    counter += 1
    if counter >= max: return False
    return True

count(1)
# Global keyword in action
limit = 5 # Make a variable call limit
for x in range(limit): # Increment a counter
    b = count(limit) # get the variable from that function using that limit
    print(counter) # Print the counter
print('Done') # Optional as showing complete



