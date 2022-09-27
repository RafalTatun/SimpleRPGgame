class Race:
    def __init__(self, extra_hp = 0, extra_mana = 0, extra_rage = 0, extra_stamina = 0):
        self.extra_hp = extra_hp
        self.extra_mana = extra_mana
        self.extra_rage = extra_rage
        self.extra_stamina = extra_stamina
    

class Human(Race):
    def __init__(self, extra_hp = 25, extra_mana = 25, extra_rage = 25, extra_stamina = 25):
        super().__init__(extra_hp, extra_mana, extra_rage, extra_stamina)


class Orc(Race):
    def __init__(self, extra_hp = 50, extra_mana = 0, extra_rage = 50, extra_stamina = 0):
        super().__init__(extra_hp, extra_mana, extra_rage, extra_stamina)


class Elf(Race):
    def __init__(self, extra_hp = 0, extra_mana = 50, extra_rage = 0, extra_stamina = 50):
        super().__init__(extra_hp, extra_mana, extra_rage, extra_stamina)


class Dwarf(Race):
    def __init__(self, extra_hp = 50, extra_mana = 25, extra_rage = 0, extra_stamina = 25):
        super().__init__(extra_hp, extra_mana, extra_rage, extra_stamina)