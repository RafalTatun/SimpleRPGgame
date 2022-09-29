#Charpter 1
import os
import printslow as ps
import character.create as character


# Story 1
text = ['Hello Adventure!\n I\'m glad to see, you feel right\n We need to hurry...\n Roof comes down','Who are me...\n Who are You?!']
player_text = ['1. Who am I?\n My head\'s about to explode...', '2. I\'m... [Creating character]']
new_character = character.Create()

# Init new character 
def init_new_character():
    os.system('cls')
    ps.print_slow(text[0])
    while True:
        for all_text in player_text: print(all_text)
        choice = input('')
        if int(choice) == 1:
            ps.print_slow(text[1])
            new_character.update_char()
            return new_character
        elif int(choice) == 2:
            new_character.update_char()
            return new_character
        else:
            print('Invalid choice, try again')
        
        # print(f'{new_character.name}\n{new_character.gender}\n{new_character.race}\n{new_character.classes}\n{new_character.healthMax}\n{new_character.manaMax}')