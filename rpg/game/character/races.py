from dataclasses import dataclass


@dataclass
class Race:
    name: str = None
    extra_hp: int = 0
    extra_mana: int = 0
    extra_rage: int = 0
    extra_stamina: int = 0


    def get_name(self):
        return self.name
    

class Human(Race):
    def __init__(self, name='Human', extra_hp = 25, extra_mana = 25, extra_rage = 25, extra_stamina = 25):
        super().__init__(name, extra_hp, extra_mana, extra_rage, extra_stamina)


class Orc(Race):
    def __init__(self, name='Orc', extra_hp = 50, extra_mana = 0, extra_rage = 50, extra_stamina = 0):
        super().__init__(name, extra_hp, extra_mana, extra_rage, extra_stamina)


class Elf(Race):
    def __init__(self, name='Elf', extra_hp = 0, extra_mana = 50, extra_rage = 0, extra_stamina = 50):
        super().__init__(name, extra_hp, extra_mana, extra_rage, extra_stamina)


class Dwarf(Race):
    def __init__(self, name='Dwarf', extra_hp = 50, extra_mana = 25, extra_rage = 0, extra_stamina = 25):
        super().__init__(name, extra_hp, extra_mana, extra_rage, extra_stamina)
        