import simpleguitk as simplegui
import random
import math

secret_number = 0
number_upper_range = 0
count = 0

# helper function to start and restart the game


def new_game():
    global secret_number, number_upper_range, count
    print('New game! Please input the upper limit.\n')


def number_range(upper_limit):
    global secret_number
    secret_number = random.randrange(0, int(upper_limit))

    global count
    count = math.ceil(math.log2(int(upper_limit) + 1))
    print('The range is [0, ' + str(upper_limit) + ').')
    print('You have', str(count), 'guesses.\n')


def input_guess(guess):
    print('Guess was', guess, '.')

    if int(guess) > secret_number:
        print('Lower')
        count_check()
    elif int(guess) < secret_number:
        print('Higher')
        count_check()
    else:
        print('Correct!!! You win!!!\n')
        new_game()
    return


def count_check():
    global count
    count -= 1
    if count > 0:
        print('You have', str(count), 'guesses remaining.\n')
    else:
        print('Out of guesses! You lose! The number is ' +
              str(secret_number) + '.\n')
        new_game()


# create frame
f = simplegui.create_frame('Guess the number', 250, 250)


# register event handlers for control elements and start frame
f.add_input('Upper limit is', number_range, 240)
f.add_input('Guessed number is', input_guess, 240)


# call new_game
new_game()
f.start()
