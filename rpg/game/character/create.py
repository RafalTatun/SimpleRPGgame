# Creating character
from .races import *
from .classes import *
from .location import *
from player import *
from dataclasses import dataclass
import json

player_save = Player()


@dataclass
class Create:
    name: str = None
    race: dict = None
    classes: dict = None
    level: int = 1
    exp: int = 0
    location: str = None
    health_max: int = 0
    mana_max: int = 0
    rage_max: int = 0
    stamina_max: int = 0


    def init_general_information(self):
        self.name = input('What is your name: ')
        return self.name


    def init_race(self):
        print('Races: \n1. Human\n2. Orc\n3. Elf\n4. Dwarf')
        while True:
            choice = int(input('Choose race: '))
            if choice == 1:
                self.race = Human()
                return self.race
            elif choice == 2:
                self.race = Orc()
                return self.race
            elif choice == 3:
                self.race = Elf()
                return self.race
            elif choice == 4:
                self.race = Dwarf()
                return self.race
            else:
                print('Invalid choice, try again')
                

    def init_class(self):
        print('Classes: \n1. Warrior\n2. Mage\n3. Rogue')
        while True:
            choice = int(input('Choose class: '))
            if choice == 1:
                self.classes = Warrior()
                return self.classes
            elif choice == 2:
                self.classes = Mage()
                return self.classes
            elif choice == 3:
                self.classes = Rogue()
                return self.classes
            else:
                print('Invalid choice, try again')


    def update_stats(self):
        self.health_max = self.race.extra_hp + self.classes.health
        self.mana_max = self.race.extra_mana + self.classes.mana
        self.rage_max = self.race.extra_rage + self.classes.rage 
        self.stamina_max = self.race.extra_stamina + self.classes.stamina
        self.level = self.level
        self.exp = self.exp


    def update_map(self):
        print('Where did you born: \n1. Town1\n2. Town2\n3. Town3')
        while True:
            choice = int(input('Choose starting location: '))
            if choice == 1:
                self.location = Town1()
                return self.location
            elif choice == 2:
                self.location = Town2()
                return self.location
            elif choice == 3:
                self.location = Town3()
                return self.location
            else:
                print('Invalid choice, try again')


    def write_json_file(self, data, filename="./save/hero.json"):
        # data[slot] = {"name":self.name, "race":self.race, "class":self.classes, }
        #DOKOŃCZYĆ WPISYWANIE DO DATA[SLOT]
        with open(filename, 'w') as fp:
            json.dump(data, fp, indent=4)       
        

        # data = data[slot]["name"].update(self.name)
        # data = data[slot]["race"].update(self.race)
        # data = data[slot]["class"].update(self.classes)
        # data = data[slot]["stats"]["health"].update(self.health_max)
        # data = data[slot]["stats"]["mana"].update(self.mana_max)
        # data = data[slot]["stats"]["raga"].update(self.raga_max)
        # data = data[slot]["stats"]["stamina"].update(self.stamina_max)
        # data = data[slot]["stats"]["level"].update(self.level)
        # data = data[slot]["stats"]["exp"].update(self.exp)


        # data[slot]["name"] = self.name
        # data[slot]["race"] = self.race
        # data[slot]["class"] = self.classes
        # data[slot]["stats"]["health"] = self.health_max
        # data[slot]["stats"]["mana"] = self.mana_max
        # data[slot]["stats"]["raga"] = self.raga_max
        # data[slot]["stats"]["stamina"] = self.stamina_max
        # data[slot]["stats"]["level"] = self.level
        # data[slot]["stats"]["exp"] = self.exp


    def update_char(self, slot):
        self.init_general_information()
        self.init_race()
        self.init_class()
        self.update_stats()
        self.update_map()
        with open("./save/hero.json") as json_file:
            data = json.load(json_file)
            data[f'Slot_{slot}']['name'] = self.name
            data[f'Slot_{slot}']['race'] = vars(self.race).get('name')
            data[f'Slot_{slot}']['class'] = vars(self.classes).get('name')
            data[f'Slot_{slot}']['health'] = self.health_max
            data[f'Slot_{slot}']['mana'] = self.mana_max
            data[f'Slot_{slot}']['rage'] = self.rage_max
            data[f'Slot_{slot}']['stamina'] = self.stamina_max
            data[f'Slot_{slot}']['level'] = self.level
            data[f'Slot_{slot}']['exp'] = self.exp
            # y = {"name": self.name, "race": self.race, "class": self.classes, "health": self.health_max, "mana": self.mana_max, "rage": self.rage_max, "stamina": self.stamina_max, "level": self.level, "exp": self.exp}
            # temp.append(y) 
        self.write_json_file(data)
        print(self.name, self.race, self.classes, self.level, self.exp, self.location, self.health_max, self.mana_max, self.rage_max, self.stamina_max)


# Tutaj skończyłeś i potrzebujesz zrobić część programu z zapisywaniem danych z Class na słownik, potem do JSON i Mapę!!! :D zapomniałem bo zacząłem robić mapę do gry w konsoli
