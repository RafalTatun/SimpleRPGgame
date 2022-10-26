# All classes
from dataclasses import dataclass


@dataclass
class Class():
    name: str = None
    health: int = 0
    mana: int = 0
    rage: int = 0
    stamina: int = 0


    def get_name(self):
        return self.name


# Class Warrior
class Warrior(Class):
    def __init__(self, name='Warrior', health=200, rage=50):
        super().__init__(name, health, rage)


# Warrior actions
    def berserker_mode(self):
        print('Charge!!!!!')
        self.damage = 30
        self.rage -= 15
        return self.rage


# Class Mage
class Mage(Class):
    def __init__(self, name='Mage', health=150, mana=100):
        super().__init__(name, health, mana)


# Mage actions
    def throw_fireball(self):
        print('Incantation FireBall!\n')
        self.damage = 50
        self.mana -= 30
        return self.damage


    def heal(self):
        print('Incantation Heal\n')
        self.heal = 30
        return self.heal


# Class Rogue
class Rogue(Class):
    def __init__(self, name='Rogue', health=100, stamina=100):
        super().__init__(name, health, stamina)


# Rogue actions
    def backstab(self):
        print('...\n')
        self.damage = 60
        self.stamina -= 50
        return self.damage


    def untouched(self):
        print('You can\'t beat me\n')
        self.stamina -= 30
        self.rndenemynumber = 10
        return self.rndenemynumber
        