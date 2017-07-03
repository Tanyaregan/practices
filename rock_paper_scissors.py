from random import randint
from time import sleep

OPTIONS = ['R', 'P', 'S']
WIN = 'You win!'
LOSE = 'You lost!'


def decide_winner(user_choice, computer_choice):
    """Picks winner between 2 choices."""

    print 'Your choice is: ' + str(user_choice)
    sleep(1)
    print 'Computer selecting...'
    sleep(1)
    print 'Computer chose: ' + str(computer_choice)

    user_choice_index = OPTIONS.index(user_choice)
    comp_choice_index = OPTIONS.index(computer_choice)

    if user_choice_index == comp_choice_index:
        print 'Its a tie!'
    elif user_choice_index == 0 and comp_choice_index == 2:
        print WIN
    elif user_choice_index == 1 and comp_choice_index == 0:
        print WIN
    elif user_choice_index == 2 and comp_choice_index == 1:
        print WIN
    elif user_choice_index > 2:
        print 'Invalid option'
        return
    else:
        print LOSE


def play_RPS():
    """Plays rock paper scissors."""
    print 'Lets play Rock, Paper, Scissors!'

    user_choice = raw_input('Select R for Rock, S for scissors or P for paper: ')
    user_choice = user_choice.upper()
    sleep(1)

    computer_choice = OPTIONS[randint(0, 2)]
    decide_winner(user_choice, computer_choice)

play_RPS()
