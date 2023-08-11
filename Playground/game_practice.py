import random

class Game:
    def __init__(self, pers_1, pers_2):
        self.pers_1 = pers_1
        self.pers_2 = pers_2
        
    def __repr__(self):
        return f'Your choosen character is {gamer}.\nYour enemy is {enemy}.\nYou can have a duel now.\n{Game.damage(self)}'
        
    def damage(self):
        a = random.randint(50, 100)
        b = random.randint(25, 50)
        if (self.pers_1 or self.pers_2) in ['Superman', 'Wanda', 'Thor', 'Hulk']:

            self.dam1 = a
            self.dam2 = a
        else:
            self.dam1 = b
            self.dam2 = b
        result = self.dam1 - self.dam2
        str1 = ['You won ', 'You lost ', 'It is a draw, neither of you won the game, please try again!']
        str2 = f'because you damaged {self.dam1} and your enemy {self.dam2}'
        if result > 0:
            return str1[0]+str2
        elif result < 0:
            return str1[1]+str2
        else:
            return str1[-1]
    
gamer_chars = ['Hulk', 'Thor', 'Wanda', 'Vision', 'Iron man', 'Superman', 'Batman', 'Flash']


gamer = input(f'Please pick a character from this list {gamer_chars}:')
enemy_chars = [name for name in gamer_chars if name !=gamer]
enemy = random.choice(enemy_chars)

game1 = Game(gamer, enemy)
print(game1)
#print(game1.__repr__())
#print(game1.damage())

    
    
        
    
    