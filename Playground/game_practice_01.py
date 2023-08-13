import time
import random

gamer_chars = ['Hulk', 'Thor', 'Wanda', 'Iron man']
gamer = input(f'Please pick a character from this list {gamer_chars}:')
enemy_chars = [name for name in gamer_chars if name !=gamer]
enemy = random.choice(enemy_chars)

class Character:
    characters = {'Hulk' : {'power':random.randint(100, 2000), 'speed':500, 'life': 200},
                  'Thor' : {'power':random.randint(100, 3000), 'speed':1000, 'life': 2000},
                  'Wanda' : {'power':random.randint(200, 4500), 'speed':250, 'life': 100},
                  'Iron man' : {'power':500, 'speed':2000, 'life': 100},
                  }
    gamers_count = 0
          
    def __init__(self, name):
        
        self.name = name
        self.attributes()
        type(self).gamers_count +=1
        
    def __repr__(self):
        return f'Your choosen character is {self.name}.\nYour randomly picked enemy is {enemy}.\nYou can have a duel now. '
    
    def attributes(self):
        self.power = type(self).characters[self.name]['power']
        self.speed = type(self).characters[self.name]['speed']
        self.life = type(self).characters[self.name]['life']
        return f'Your character power is {self.power}, your speed is {self.speed}, your life value is {self.life}'
    

game1 = Character(gamer)
game2 = Character(gamer)
game3 = Character(gamer)
game4 = Character(gamer)

print(game1)
print(game1.attributes())
print(f'We got {Character.gamers_count} players registered')

class Game:
    def __init__(self, gamer, enemy):
        self.Character.name = gamer
        self.enemy = enemy
