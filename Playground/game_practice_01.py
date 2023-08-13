import time
import random

gamer_chars = ['Hulk', 'Thor', 'Wanda', 'Vision', 'Iron man', 'Superman', 'Batman', 'Flash']
gamer = input(f'Please pick a character from this list {gamer_chars}:')
enemy_chars = [name for name in gamer_chars if name !=gamer]
enemy = random.choice(enemy_chars)

class Character:
    gamers_count = 0
    
    def __init__(self, name):
        
        self.name = name
        type(self).gamers_count +=1
    
    def char(self):
        if self.name == 'Superman':
            self.power = 1000
            self.speed = 300
            return f"Your character {self.name}'s power is {self.power} and your speed is {self.speed} thousand km/hrs."
            

    def __repr__(self):
        return f'''Your choosen character is {self.name}.\nYour randomly picked enemy is {enemy}.\nYou can have a duel now. 
Your power is {self.power}, your speed is {self.speed}'''
    

game1 = Character(gamer)
game2 = Character(gamer)
game3 = Character(gamer)
game4 = Character(gamer)

print(game1)
print(f'We got {Character.gamers_count} players registered')
