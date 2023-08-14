import random as rm
#Marvel vs DC Universe

gamer_chars = ['Hulk', 'Thor', 'Iron man', 'Superman', 'Black Adam', 'Batman']
gamer = input(f'Please select your character from this list {gamer_chars}:')

class Character:
    
    a, b = rm.randint(100, 2000), rm.randint(200, 4000)
    c, d = rm.randint(10, 500), rm.randint(50, 2500)
    
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
        Character.gamers_count +=1
        
    def __repr__(self):
        return f'Your choosen character is {self.name}.'
    
    def attributes(self):
        self.power = type(self).characters[self.name]['power']
        self.speed = type(self).characters[self.name]['speed']
        self.life = type(self).characters[self.name]['life']
        return f'Stats: power: {self.power}, speed: {self.speed}, life value: {self.life}'
    
    def damage(self):
        self.damage = self.power*0.4 + self.speed*0.4 + self.life*0.2
        return f'You cause {int(self.damage)} amount of damage in a round.'

#Test
gamer1 = Character(gamer)
gamer2 = Character('Thor')

print(gamer1)
print(gamer1.attributes())
print(gamer1.damage())
#print(f'We got {Character.gamers_count} players registered')

enemy_chars = [name for name in gamer_chars if name != gamer]
enemy = input(f'Please select your enemy from this list {enemy_chars}:')

class Game:
    
    def __init__(self, enemy):
        self.enemy = enemy
        
    def __repr__(self):
        return f'Your enemy is {self.enemy}. You can start battling.'
    
    def attributes(self):
        self.attributes = Character(self.enemy).attributes()
        return self.attributes
    
    def damage(self):
        self.damage = Character(self.enemy).damage()
        return self.damage
        
print(Game(enemy).attributes())
print(Game(enemy).damage())
