import random

class Character:
    def __init__(self, name : str, power: int, speed: int, life:int):
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
    
    def __init__(self):
        self.player = False
        self.enemy = False
        
    def addPlayer(player: Character):
        self.player = player

    def addEnemy(enemy:  Character):
        self.enemy = enemy
    
gamer_chars = ['Hulk', 'Thor', 'Wanda', 'Vision', 'Iron man', 'Superman', 'Batman', 'Flash']


gamer = input(f'Please pick a character from this list {gamer_chars}:')
enemy_chars = [name for name in gamer_chars if name !=gamer]
enemy = random.choice(enemy_chars)

game1 = Game()
#Some testing
#print(game1.damage())
print(game1)

#print(help(Game))

    
    
        
    
    