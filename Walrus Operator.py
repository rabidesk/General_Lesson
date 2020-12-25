"""Walrus operator and global
Added in Python 3.8 or higher
Assign a variable from an expression, it works only right version."""
# Walrus operator super convenient and super first
# Assign a variable from an expression
# Must have the right version!
# Common issue()
#y := len('Hello')
(y := len('Hello')) # valid but not recommended bkz it confusing
print(y)

folk = ['Sunny', 'Lemo', 'Fary'] # Make a list
if (n := len(folk)) <=3: print(n) # Less then or equal to 3 then it will printout, it will show length
# Simple Example
lines = []

def  canAdd(max=5):
    global lines # Allows us to ensure we are using the global variable

    if allowed := (count :=len(lines))<max:  # function len to get length of lines that done by allowed with
                                         # walrus operator for expression, it also provide get sign to variable
        print(f'You can enter {max - count} more')
    return allowed # Allowed

while canAdd():
    lines.append(l := input('Enter a line:'))
print(f'You entered:{lines}')


