# For loop and range
# For loop on lists, tuples, sets
# l = [1, 2, 3, 4]  # List
# t = (1, 2, 3, 4)  # Tuple
# s = {1, 2, 3, 4}  # set
#
# for i in s:  # something like while loop and we are creating a variable in statement itself
#     print(f'i = {i}')  # Base on the x value it can run only for i
# x = dict(Hena=45, Tamy=44, Heala=33, Cheri=22)  # Simple crate dictionary
# print(x)
# # Any method can do as you like
# for k in x.keys():  # It say each one of those get the value
#     print(f'Keys: {k}= {x[k]} ')  # The first k mean the name and second k mean the actual value as set
# for k, v in x.items():  # Call the items function to get the all value from the dictionary
#     print(f'Items: {k}= {v}')  # K is item name and v is value

# Range
# x = range(7)
# print(x)
# for i in x:  # For loop will be auto increment to know the value of x
#     print(f'Value of range for X is:{i}')  # Get the result.
# # Range will be start, stop & stepping
# x = range(5, 21, 3)  # It start from 5, stop in range 20 and sequence 3
# for i in x:
#     print(f'Value of stepping for X is:{i}')  # Value of stepping result will be generated

# Boolean Ture or False
# x = True  # Case sensitive
# y = False  # Case sensitive
# '''
# Practice some comparison operator
# '''
# print(f'x={x}')
# print(f'y={y}')
#
# print(f'Equal:{x==y}')
# print(f'Not Equal:{x!=y}')
#
# print(f'Grater than operator:{x>y}')
# print(f'Grater than or equal  :{x>=y}')
#
# print(f'Less than operator:{x<y}')
# print(f'Less than or equal  :{x<=y}')

#  Conditional operator in if-else statement
# exam_marks: int = int(input("What is your exam marks: "))
#
#
# def show_marks(grade):
#     print(f'Your result:{grade}')
#
#
# if exam_marks > 80:
#     show_marks("A+")
# elif 80 > exam_marks >= 70:
#     show_marks("A")
# elif 70 > exam_marks > 60:
#     show_marks("A-")
# elif 60 > exam_marks >= 50:
#     show_marks("B+")
# elif 50 > exam_marks >= 40:
#     show_marks("c")
# elif exam_marks > 33:
#     show_marks("Pass")
# else:
#     show_marks("F Grad")
# print('Finished')

# Nested if-else statement
# exam_marks = int(input("What is your marks ?"))
# good_user = 70 > 60 # Boolean expression define the true or false
# print(good_user)  # Print either true or false
# def show_marks(grade):       # variable declaration
#     print(f'Your result in grade:{grade}')
#
# if exam_marks > 80 or exam_marks > 40:  # First if condition
#     print("Your marks is very good ")
#     if exam_marks <  80:                  # Second if condition
#         print('Excellent Result')
#     # elif exam_marks > 40:
#     else:
#         print('Result is not good')
# else:                                       # Second else statement
#     show_marks("passed or F grade")
#
# number = int(input("Insert your number"))
#
# good_user = number >= 80
#
# print(f'The number is :{good_user}')

# Loop functions with if-else statements
# def is_even(number): # declear the variable is_even & number is argument
#     if number % 2 == 0: # checkout the number divided by 2 for getting the value true or false
#         return True
#     else:
#         return False
#
# starting = 0  # declare the variable that start from 0
# while starting <= 10: # While loop is declare to count the number as given here
#     if is_even(starting): # Check the number based on the argument
#         print(f'{starting} is even') # Print variable value as odd or even
#     else:
#         print(f'{starting} is odd')
#     starting = starting + 1 # Increment operation
# print("Program is completed")

#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# even_number = [] # Can identify only even numbers
# starting = 0 # Starting value
# user_input = int(input("Check Number:")) # Get input from the user
# while starting<user_input: # Start the while loop based on user input
#     if is_even(starting): # if condition will check the even number
#         even_number.append(starting) # append function insert the even number to define even value
#     starting = starting +1 # Increment operation
# print(f'Even numbers: {even_number}') # Result of even number
# print("Program is completed") # program is completed

#
# from tkinter import *
# import time
#
# def tick():
#     time_string = time.strftime("%I:%M:%S %D") # Time frame
#     clock.config(text = time_string) # Clock configuration
#     clock.after(200,tick) # counting timeframe
#
# root = Tk() # root function
#
# clock = Label(root, font = ("Arial", 50), fg="#00FF00", bg = "black") # Display background
# clock.grid(row =0, column = 1) # Display configuration
# tick()
# root.mainloop()




A = "python"
B = "nohtyp"
A1 = A.reverse()
if A1 == B:
    print(1)
else:
    print(A1)





