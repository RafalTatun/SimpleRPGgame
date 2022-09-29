# Main menu
import time
import os
import printslow as ps
import charpter1

text1 = ['Game title', 'Game made by Rafal Tatun']
menu_text = ['1. New Game', '2. Online (comming soon)', '3. Load Game (comming soon)', '4. Exit']


def main_menu():
    ps.print_slow(text1[0])
    ps.print_slow(text1[1])
    time.sleep(2)
    os.system('cls')
    for i in range(len(menu_text)): ps.print_slow(menu_text[i])
    while True:
        new_character = charpter1.new_character
        slot1 = 'Slot'
        slot2 = 'Slot'
        slot3 = 'Slot'
        choice = input('Select option: ')
        if int(choice) == 1:
            os.system('cls')
            print(f'Slots:\n1. {slot1}\n2. {slot2}\n3. {slot3}')
            choice = input('Select option: ')
            if int(choice) == 1:
                charpter1.init_new_character()
                slot1 = charpter1.character.Create.name
            elif int(choice) == 2:
                charpter1.init_new_character()
                slot2 = charpter1.character.Create.name
            elif int(choice) == 3:
                charpter1.init_new_character()
                slot3 = charpter1.character.Create.name
            else:
                print('No more slots. Try again')
            print(f'{new_character.name}\n{new_character.gender}\n{new_character.race}\n{new_character.classes}\n{new_character.health_max}\n{new_character.mana_max}')
            print(f'Slots:\n1. {slot1}\n2. {slot2}\n3. {slot3}') 
            break
        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            pass
        elif int(choice) == 4:
            break
        else:
            print('Invalid choice, try again') 