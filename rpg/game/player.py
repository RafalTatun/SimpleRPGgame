# Information about him
# 
# Name
# Race
# Class
# Profession
# Location
# Backpack
#
# Menu player:
# check Quest
# check Map
# Inventory
# Exit
import os
import json
from dataclasses import dataclass


json_file = open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/save/hero.json", "r")
data_slot = json.load(json_file)

@dataclass
class Player:
    def stats(self, slot):
        return data_slot[slot]


    def save(self, hero):
        data_hero = json.dumps(hero, indent=4)
        json_file.write(data_hero)
        json_file.close()


    def load(self, hero):
        json.dumps(hero, indent=4)


    def show_quests(self):
        pass


    def show_inventory(self):
        pass


    def experience(self, enemy_lvl):
        return self.exp * enemy_lvl

    
    def menu_player(self):
        os.system('cls')
        os.system('clear')
        choice = int(input('1. Quests\n2. Inventory\n3. Save\n4. Load\n5. Exit\nSelect option: '))
        if choice == 1:
            self.show_quests()
        elif choice == 2:
            self.show_inventory()
        elif choice == 3:
            pass
            self.save()
        elif choice == 4:
            pass
            load()
        elif choice == 5:
            exit()
        else:
            print('Invalid choice, try again')


    # def menu_action(self):
    #     if input('What do you want to do? ')=='menu':
    #         self.menu_player()
    #     elif input('What do you want to do? ')=='talk':
    #         pass
    #     elif input('What do you want to do? ')=='attack':
    #         self.experience()
    #     elif input('What do you want to do? ')=='run':
    #         pass
    #     elif input('What do you want to do? ')=='move':
    #         pass
    #     else:
    #         print('Invalid choice, try again')