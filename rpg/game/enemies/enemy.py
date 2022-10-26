import json
from dataclasses import dataclass


json_file = open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/enemies/data.json", 'r')
data_enemies = json.load(json_file)

@dataclass
class Enemy():
    name: str = None
    lvl: int = 1
    exp_hero: int = 0
    health: int = 0
    mana: int = 0
    rage: int = 0
    stamina: int = 0



class Troll(Enemy):
    def __init__(self, name=data_enemies["Troll"]["name"], health=data_enemies["Troll"]["health"], rage=data_enemies["Troll"]["rage"], level=data_enemies["Troll"]["lvl"]):
        self.name = name
        self.health = health
        self.rage = rage
        self.level = level
    

    def smash(self):
        print('Ghaarr!')
        self.damage = 20
        self.rage -= 50
        return self.damage

    def angry(self):
        print('Aaaaa!!!')
        self.rage += 20
        return self.rage