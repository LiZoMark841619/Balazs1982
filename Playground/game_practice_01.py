import random as rm
#Marvel vs DC Universe

gamer_chars = ['Hulk', 'Thor', 'Iron man', 'Superman', 'Black Adam', 'Batman']
gamer = input(f'Please pick your character from this list {gamer_chars}:')
enemy_chars = [name for name in gamer_chars if name != gamer]
enemy = input(f'Please pick your enemy from this list {enemy_chars}:')

class Character:
    
    a = rm.randint(100, 2000)
    b = rm.randint(200, 4000)
    c = rm.randint(10, 500)
    d = rm.randint(50, 2500)
    
    characters = {'Hulk' : {'power':b, 'speed':c, 'life': 100},
                  'Thor' : {'power':b, 'speed':d, 'life': 3000},
                  'Iron man' : {'power':a, 'speed':d, 'life': 100},
                  'Superman' : {'power':b, 'speed':d, 'life': 100},
                  'Black Adam' : {'power':b, 'speed':d, 'life': 3000},
                  'Batman' : {'power':a, 'speed':c, 'life': 100}
                  }
    
    gamers_count = 0
          
    def __init__(self, name):
        self.name = name
        self.attributes()
        type(self).gamers_count +=1
        
    def __repr__(self):
        return f'Your choosen character is {self.name}.'
    
    def attributes(self):
        self.power = type(self).characters[self.name]['power']
        self.speed = type(self).characters[self.name]['speed']
        self.life = type(self).characters[self.name]['life']
        return f'Your character power is {self.power}, your speed is {self.speed}, your life value is {self.life}'

#Test
gamer1 = Character(gamer)
gamer2 = Character('Thor')
gamer3 = Character('Iron man')

print(gamer1)
print(gamer1.attributes())
print(f'We got {Character.gamers_count} players registered')

class Game:
    def __init__(self, gamer, enemy):
        self.gamer = gamer
        self.enemy = enemy
        
    def damage(self):pass