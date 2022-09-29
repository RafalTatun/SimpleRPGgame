# Main menu
import time
import os
import printslow as ps
import charpter1

new_character = charpter1.new_character
text1 = ['Game title', 'Game made by Rafal Tatun']
menu_text = ['1. New Game', '2. Online (comming soon)', '3. Load Game (comming soon)', '4. Exit']

def main_menu():
    ps.print_slow(text1[0])
    ps.print_slow(text1[1])
    time.sleep(2)
    os.system('cls')
    for i in range(len(menu_text)): ps.print_slow(menu_text[i])
    while True:
        choice = input('Select option: ')
        if int(choice) == 1:
            os.system('cls')
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