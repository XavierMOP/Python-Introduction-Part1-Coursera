# Rock-Paper-Scissors-Lizard-Spock
# Use "return" to end a function

import random


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "NOOOOOO"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"


def rpsls(player_choise):
    print("The player's choise is", str(player_choise)+".")
    player_number = name_to_number(player_choise)
    # print player_number
    computer_number = random.randrange(0, 4)
    computer_choise = number_to_name(computer_number)
    print("The computer's choise is", str(computer_choise)+".")
    if computer_number == player_number:
        print("Tie!")
    elif (computer_number - player_number) % 5 == 1 or (computer_number - player_number) % 5 == 2:
        print("Computer wins!")
    elif (computer_number - player_number) % 5 == 3 or (computer_number - player_number) % 5 == 4:
        print("Player wins!")
    else:
        return
    print("")


rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("Spock")


def number_to_fortune(num):
    if num == 0:
        return "Yes, for sure!"
    elif num == 1:
        return "Probably yes."
    elif num == 2:
        return "Seems like yes..."
    elif num == 3:
        return "Definitely not!"
    elif num == 4:
        return "Probably not."
    elif num == 5:
        return "I really doubt it..."
    elif num == 6:
        return "Not sure, check back later!"
    elif num == 7:
        return "I really can't tell"
    else:
        return "Something was wrong with the input."

# Test help func
# print (number_to_fortune(0))
# print (number_to_fortune(1))
# print (number_to_fortune(2))
# print (number_to_fortune(3))
# print (number_to_fortune(4))
# print (number_to_fortune(5))
# print (number_to_fortune(6))
# print (number_to_fortune(7))
# print (number_to_fortune(9))


def mystical_octosphere(question):
    print('Your question is : '+question)
    print('You shake the mystical octosphere!')
    answer_number = random.randrange(0, 7)
    answer_fortune = number_to_fortune(answer_number)
    print('The cloudy liquid swirls, and a reply comes into view...')
    print('The mystical octosphere says...' + answer_fortune)
    print('')


mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")
mystical_octosphere('Is Zeef a pervert?')
mystical_octosphere('Is Xavier a pervert?')
mystical_octosphere('Is Zeef a bad guy?')
mystical_octosphere('Is Xavier a bad guy?')
