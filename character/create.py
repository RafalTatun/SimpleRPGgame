# Creating character

import os
import json
from .races import *
from .classes import *
from .location import *
from .professions import *
from enum import Enum


hero = {
    'name': '',
    'sex': '',
    'race': '',
    'classes': '',
    'health': 0,
    'mana': 0,
    'rage': 0,
    'stamina': 0,
    'profession': ''
}


class Create:
    def __init__(self, name = None, gender = None, race = None, classes = None, location = None, health_max = 0, mana_max = 0, rage_max = 0, stamina_max = 0, profession = None):
        self.name = name
        self.gender = gender
        self.race = race
        self.classes = classes
        self.location = location
        self.health_max = health_max
        self.mana_max = mana_max
        self.rage_max = rage_max
        self.stamina_max = stamina_max
        self.profession = profession


    def init_general_information(self):
        self.name = input('What is your name: ')
        self.gender = input('What is your gender: ')
        os.system('cls')
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
            os.system('cls')
                

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
            os.system('cls')


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

        with open('hero.txt', 'w') as json_file:
            json.dump(hero, json_file)


# Tutaj skończyłeś i potrzebujesz zrobić część programu z zapisywaniem danych z Class na słownik, potem do JSON i Mapę!!! :D zapomniałem bo zacząłem robić mapę do gry w konsoli


