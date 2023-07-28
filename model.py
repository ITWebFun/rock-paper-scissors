import random
choices = ('Rock', 'Paper', 'Scissors')

class Player:
    def __init__(self,name='Computer',score=0):
        self.name = name
        self.score = score
        self.choice = ''
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_score(self):
        return self.score
    
    def increase_score(self):
        self.score += 1
        
    def set_choice(self, choice=None):
        if not choice:
            choice = random.choice(choices)
        print(choice)
        self.choice = choice
        
    def get_choice(self):
        return self.choice