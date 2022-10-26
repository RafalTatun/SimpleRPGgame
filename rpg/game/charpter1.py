#Charpter 1
import os
import printslow as ps
from character import *
from npc.npc import malcolm

# Story 1
new_character = create.Create()


# Init new character 
def init_new_character(slot):
    os.system('cls')
    os.system('clear')
    ps.print_slow('Charpter 1\n"Headache"')
    ps.print_slow(malcolm.get_text[0])
    while True:
        ps.print_slow(malcolm.get_text[1])
        choice = input('Select option: ')
        if int(choice) == 1:
            ps.print_slow(malcolm.get_text[2])
            new_character.update_char(slot)
        elif int(choice) == 2:
            new_character.update_char(slot)
        else:
            print('Invalid choice, try again')
            
        # print(f'{new_character.name}\n{new_character.gender}\n{new_character.race}\n{new_character.classes}\n{new_character.healthMax}\n{new_character.manaMax}')