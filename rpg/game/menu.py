# Main menu
import time
import os
import printslow as ps
import charpter1


menu_text = ['1. New Game', '2. Load Game (comming soon)', '3. Online (comming soon)', '4. Exit']


def main_menu():
    ps.print_slow('\nGame title\n\nGame made by Rafal Tatun')
    time.sleep(2)
    os.system('cls')
    os.system('clear')
    ps.print_slow('1. New Game\n\n2. Load Game (comming soon)\n\n3. Online (comming soon)\n\n4. Exit')
    while True:
        new_character = charpter1.new_character
        choice = input('Select option: ')
        if int(choice) == 1:
            os.system('cls')
            os.system('clear')
            charpter1.init_new_character()
            print(f'{new_character.name}\n{new_character.gender}\n{new_character.race}\n{new_character.classes}\n{new_character.health_max}\n{new_character.mana_max}')
            break
        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            pass
        elif int(choice) == 4:
            break
        else:
            print('Invalid choice, try again') 