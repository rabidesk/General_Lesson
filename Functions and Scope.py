"""
Function and Scope many programming language used.
Lexical scope sometimes known as static scope
(Range of functionality) can all be called in the block of code
However, Scope can be nested inside another
"""
# This is the global scope
name = "Suny Dewy"


# Functions can access the global scpe
def test1():
    print(f'My name is {name}')


test1()  # Call the function as define test1()
# Global scpe can't access function scope
x = 10  # This is global scope


def test2():
    x = 55  # This is local scope , even though same name but two different scope
    print(f'Function scope {x}')


test2()
print(f'Global Scope {x}')
# Global scope > function scope > statement
x = 20  # Fist variable for global scope
print(f'Global x value:{x}')


def test3():  # It's block of code of it's own individual little scope, fist it goes global then function then statement
    x = 0  # Second variable for function scope
    print(f'Function scope value {x}')
    for i in range(3):
        x += 1  # 3 layers down the value bit higher by adding
        y = x * i  # another value of Y define from calculation
        print(f'Statement x:{x}')
        print(f'Statement Y:{y}')  # It will count the value upto range as mention in argument 3
    print(f'Function Scope x:{x}')
    print(f'Function Scope Y:{y}')  # This could be issue if use multiple time


test3()  # call the scope
print(f'Global Scope x:{x}')


# print(f'Global Scope Y:{y}')  # This fine the global scope is not define bkz Y can't define in this scope except X
# Function do not share scope with each other bkz they are individual to each other so can not share
def bus():
    z = 1  # Only exist in the function


def car():
    z = 3  # Only exist in the function
    print(z)


bus()
car()  # can print only 3 that mean they do not share scope each other


# Functions can not return value, How do you share information between function

def numbers(steps):  # Define this function as parameter steps
    l = range(1, 20, steps)  # l is range using step
    for i in l:  # for loop all the information as generated
        print(i)
    return l


def lotto():  # lotto function
    z = numbers(3) # Step of 3 , that number exist in global variable
    for x in z: # for loop find the number as define in x
        print(f'Lucky number {x}')


lotto()
