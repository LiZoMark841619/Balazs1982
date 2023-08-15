import random

class Character:
    def __init__(self, name, power, speed, life):
        self.name = name
        self.power = power
        self.speed = speed
        self.life = life
        
class Hulk(Character):
    def __init__(self):
        super().__init__(name = "Hulk", power = 1000, speed = 500, life = 100)
        
class Thor(Character):
    def __init__(self):
        super().__init__(name = "Thor", power = 1500, speed = 1000, life = 3000)

class Superman(Character):
    def __init__(self):
        super().__init__(name = "Superman", power = 2000, speed = 2000, life = 100)
    
class Game:
    
    def __init__(self, player, enemy):
        self.player = False
        self.enemy = False
        
    def addPlayer(self, player):
        self.player = player

    def addEnemy(self, enemy):
        self.enemy = enemy
    
gamer_chars = ['Hulk', 'Thor', 'Superman']

char1 = Hulk().speed
game1 = Game('Thor', 'Hulk').addEnemy('Hulk')
print(char1)
print(game1)
    
        
    
    