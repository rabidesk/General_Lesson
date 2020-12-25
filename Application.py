# Simple app - paint calculator
# How much water is need to wash
print('Water calculator')
print('Enter a size of room for floor or press enter to stop')
print('Example: 12,8')
# Variables
floor = []  # Find the measurement
gallons = 1 / 350  # One gallon covers 350 feets
total = 0  # Total gallons to buy
# Get the user input
while True:  # To create while loop to test when we need breakout of this loop
    s = input('Enter a floor size:')
    if len(s) == 0: break
    # Verify the input
    sqft = s.split(',')  # String is multiple value that based on spilt on sequence of character
    if len(sqft) < 2: # it can return less than 2
        print('Invalid format') # Return to invalid format
        break
# Converting string to integer bkz we have to work with integer number
    w = int(sqft[0])
    l = int(sqft[1])
    item = [w,l]
    floor.append(item) # This is list folder of floor dimension
    print(f'Adding wall dimension: {item}')
# Calculate the number
print(f'You entered {floor}')
for m in floor:
    w = m[0]
    l = m[1]
    s =  w * l # Create another variable
    v = s * gallons # Calculate the total number of water
    total += v # Final calculation of water
print(f'You need take water {round(total,2)} gallons for wash')


