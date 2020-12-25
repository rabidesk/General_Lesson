'''
Author: Rabi
Topic: Random Number Generation
'''

import random # Can generate random number
play_number = 'n' # get the variable

while play_number == 'n':
    number_answer = random.randint(1,10) # Numebr answer can be generate 1 to 100
    get_number = input('Guessing your number in between 1 to 10:')
    get_number = int(get_number)
    counter = 1

    while get_number != number_answer:
        if get_number > number_answer:
            print('Your number is to higher than guessing number')
        if get_number <number_answer:
            print('Your number is lower than guessing number')
        get_number = int(input('Guessing number in between 1 - 10:'))

        counter = counter +1

    print('You find your guessing number! after ' + str(counter) + ' times')
    play_number = input('Continue?')




