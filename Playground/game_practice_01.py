import time
import random

gamer_chars = ['Hulk', 'Thor', 'Wanda', 'Vision', 'Iron man', 'Superman', 'Batman', 'Flash']
gamer = input(f'Please pick a character from this list {gamer_chars}:')
enemy_chars = [name for name in gamer_chars if name !=gamer]
enemy = random.choice(enemy_chars)

class Character:
    
    gamers_count = 0
          
    def __init__(self, name, power, speed, life=100):
        
        self.name = name
        self.power = power
        self.speed = speed
        self.life = life
        type(self).gamers_count +=1
        
    def __repr__(self):
        return f'''Your choosen character is {self.name}.\nYour randomly picked enemy is {enemy}.\nYou can have a duel now. 
Your power is {self.power}, your speed is {self.speed}'''
    

game1 = Character(gamer, 100, 10)
game2 = Character('Balazs', 50, 10)
game3 = Character('Thor', 200, 5)
game4 = Character('Superman', 50, 10)

print(game1)
print(f'We got {Character.gamers_count} players registered')

class Game:
    pass