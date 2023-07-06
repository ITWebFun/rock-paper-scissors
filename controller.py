from model import *

user, computer = Player(), Player()

def set_user_name(username):
    user.set_name(username)

def play(choice):
    user.set_choice(choice)
    computer.set_choice()
    
    user_choice = user.get_choice()
    pc_choice = computer.get_choice()
    
    if (user_choice == 'Rock' and pc_choice == 'Scissors') \
        or (user_choice == 'Paper' and pc_choice == 'Rock') \
        or (user_choice == 'Scissors' and pc_choice == 'Paper'):
        user.increase_score()
        return f'{user.get_name()} wins!'
    elif user_choice == pc_choice:
        computer.increase_score()
        return 'It\'s a tie!'
    else:
        return 'The computer won!'