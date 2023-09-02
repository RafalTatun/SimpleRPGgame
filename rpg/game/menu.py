# Main menu
import time
import os
import json
import printslow as ps
from charpter1 import new_character, init_new_character


menu_text = ['1. New Game', '2. Load Game (comming soon)', '3. Online (comming soon)', '4. Exit']

json_file = open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/save/hero.json", "r")
data_slot = json.load(json_file)


def main_menu():
    ps.print_slow('\nGame title\n\nGame made by Rafal Tatun')
    time.sleep(2)
    os.system('clear')
    os.system('cls')
    ps.print_slow('1. New Game\n\n2. Load Game (comming soon)\n\n3. Online (comming soon)\n\n4. Exit')
    while True:
        choice = input('Select option: ')
        if int(choice) == 1:
            os.system('clear')
            os.system('cls')
            slot(choice)
        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            pass
        elif int(choice) == 4:
            break
        else:
            print('Invalid choice, try again')


def slot(slot):
    print(os.system("ls ./save"))
    match slot:
        case 1:
            init_new_character(slot)
        case 2:
            init_new_character(slot)
        case 3:
            init_new_character(slot)
        case _:
            return 'Invalid choice, try again'
    # if int(input('Select option: ')) == 1:
    #     init_new_character(slot)
    #     data_slot['Slot_1']['name'] = new_character.name
    # elif int(input('Select option: ')) == 2:
    #     init_new_character(slot)
    #     data_slot['Slot_2']['name'] = new_character.name
    # elif int(input('Select option: ')) == 3:
    #     init_new_character(slot)
    #     data_slot['Slot_3']['name'] = new_character.name
    # else:
    #     print('Invalid choice, try again')


def load():
    json_file.read()