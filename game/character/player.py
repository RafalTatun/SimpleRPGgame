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
# Inventory
# Save
# Load
# Exit
import os

def show_quests():
    pass


def show_inventory():
    pass


def save():
    pass


def load():
    pass


def exit():
    pass


class Player:
    def menu_player(self):
        while True:
            os.system('cls')
            choice = input('1. Quests\n2. Inventory\n3. Save\n4. Load\n5. Exit\n')
            if choice == 1:
                show_quests()
            elif choice == 2:
                show_inventory()
            elif choice == 3:
                save()
            elif choice == 4:
                load()
            elif choice == 5:
                exit()
            else:
                print('Invalid choice, try again')

hero = Player()

hero.menu_player()