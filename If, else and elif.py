"""
If, else and elif this is actually basic building building block as flow of control
"""
# Create if Condition
x = False
if x:  # Previous line find that x is not ture then ignore the line of 7 and 8, it can only print line 10
    print('Yes')
    print('Again')
else:
    print('Hello!!!')
# Condition Evaluations ( True - run | False - Not run )
x = 100
y = 25
# Base on such type logic computer can understand
if y == x: print('This is equal to ')  # It can not be print bkz not follow the condition
if y != x: print('Not equal to  ')  # It can be print bkz condition is matching
if y < x: print('This is less than ')  # It can be print bkz condition is matching
if y > x: print('Greater than ')  # It can not be print bkz not follow the condition
if y <= x: print('Less then or equal to')  # It can be print bkz condition is matching
if y >= x: print('Greater then or equal to')  # It can not be print bkz not follow the condition

# Elif is the switch solution super easy to follow the following code rather previous code
x = 10
if x == 25:
    print('X = 30')
elif x == 30:
    print('X = 30')
elif x == 100:
    print('X = 100')
else:  # If we didn't fine any switching statement then we can say else
    print('None of matching')

# Nested Statements if you didn't like elif
# This is basically statement of statement of statement as you can go ever
x = 82
if x > 50:
    print('Over 50')
    if x > 60:
        print('Over 60')
        if x > 70:
            print('Over 70')
            if x > 80:
                print('Over 80')
                if x > 90:
                    print('Over 90')
                    if x >= 100:
                        print('Complete')