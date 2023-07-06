import random
choices = ['Rock', 'Paper', 'Scissors']

class Player:
    def __init__(self,name='Computer',score=0, choice=random.choice(choices)):
        self.name = name
        self.score = score
        self.choice = choice
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_score(self):
        return self.score
    
    def increase_score(self):
        self.score += 1
        
    def set_choice(self, choice=random.choice(choices)):
        self.choice = choice
        
    def get_choice(self):
        return self.choice

"""
def get_computer_choice():
    return random.choice(choices)

user_score = 0

def get_user_score():
    return user_score

def increase_user_score():
    user_score += 1
    
pc_score = 0

def get_pc_score():
    return pc_score

def increase_pc_score():
    pc_score += 1
    
user_name = ''

def get_user_name():
    return user_name

def set_user_name(name):
    user_name = name"""