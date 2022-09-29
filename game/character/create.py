# Creating character

import os
import json
from tokenize import String
from .races import *
from .classes import *
from .location import *
from .professions import *
from dataclasses import dataclass


@dataclass
class Create:
    name: str = None
    gender: str = None
    race: str = None
    classes: str = None
    profession: str = None
    location: str = None
    health_max: int = 0
    mana_max: int = 0
    rage_max: int = 0
    stamina_max: int = 0


    def init_general_information(self):
        self.name = input('What is your name: ')
        self.gender = input('What is your gender: ')
        return self.name, self.gender


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
            os.system('cls')


    def update_char(self):
        self.init_general_information()
        self.init_race()
        self.init_class()
        self.update_map()
        self.health_max = self.race.extra_hp + self.classes.health
        self.mana_max = self.race.extra_mana + self.classes.mana
        self.rage_max = self.classes.rage
        self.stamina_max = self.classes.stamina


# Tutaj skończyłeś i potrzebujesz zrobić część programu z zapisywaniem danych z Class na słownik, potem do JSON i Mapę!!! :D zapomniałem bo zacząłem robić mapę do gry w konsoli


