import random
import time
start = time.time()

class Game:
    def __init__(self, pers_1, pers_2):
        self.pers_1 = pers_1
        self.pers_2 = pers_2
        
    def __repr__(self):
        return f'Your choosen character is {gamer}.\nYour randomly picked enemy is {enemy}.\nYou can have a duel now.\n{Game.damage(self)}'
        
    def damage(self):
        if (self.pers_1 or self.pers_2) in ['Superman', 'Wanda', 'Thor', 'Hulk']:
            self.dam1 = random.randint(50, 100)
            self.dam2 = random.randint(50, 100)
        else:
            self.dam1 = random.randint(10, 20)
            self.dam2 = random.randint(10, 20)
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
#Some testing
#print(game1.damage())
print(game1)

end = time.time()
print(end-start)
#print(help(Game))

    
    
        
    
    