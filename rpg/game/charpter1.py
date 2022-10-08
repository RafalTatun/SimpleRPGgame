#Charpter 1
import os
import printslow as ps
import character.create
from npc.npc import malcolm
import player

# Story 1
new_character = character.create.Create()


# Init new character 
def init_new_character():
    os.system('cls')
    os.system('clear')
    ps.print_slow('Charpter 1\n"Headache"')
    ps.print_slow(malcolm.get_text[0])
    while True:
        ps.print_slow(malcolm.get_text[2])
        choice = input('Select option: ')
        if int(choice) == 1:
            ps.print_slow(malcolm.get_text[1])
            new_character.update_char()
            return player.save(new_character)
        elif int(choice) == 2:
            new_character.update_char()
            return player.save(new_character)
        else:
            print('Invalid choice, try again')
        
        # print(f'{new_character.name}\n{new_character.gender}\n{new_character.race}\n{new_character.classes}\n{new_character.healthMax}\n{new_character.manaMax}')
