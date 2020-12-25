# While loop
# Loop
x = 0
while x < 10:  # It means this loop executed as long as the condition reaching true as it is 10 here
    x += 1
    print(f'x={x}')
print('Test 1 is done')
# Pass
# x = 0
# while x < 10: # Easy way to create a simple infinite loop just put pass
#     pass  # Pass is special function in python that tell continue as normally do.
# print('Test 2 is done')  # That mean it can create infinite loop here
# Continue and break
x = 0
while True:  # while evaluate True then doing the loop until this is no longer true or loop forever as infinite loop
    x += 1;
    if x < 5: # It will say if x is less than 5 print it out and go back to beginning
        print(f'x<5{x}')
        continue  # Continue say go back beginning as normally do as flow of the loop
    print(f'Do something{x}')

    if x == 10:
        print(f'Existing x ={x}')
        break # Break mean out of that flow from the loop
print('Complete')




