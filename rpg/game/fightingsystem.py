from enemies.enemy import Troll
from player import Player
import random


enemy1 = Troll()
player = Player()
#Showing stats before and after fight
def stats():
    print(f'Your enemy\nName: {player.stats("Slot_1")}\n')
    print(f'Your enemy\nName: {enemy1.name}\nHealth: {enemy1.health}\nRage: {enemy1.rage}\nLevel: {enemy1.level}\n')


#Fighting system
def fighting_system():
    while True:
        rndnumber = 1
        rndenemynumber = 3
        print(f'Hero number: {rndnumber}\n Enemy number: {rndenemynumber}')
        stats()
        if input('What to do? ')=='attack':
            #Hero attack
            if rndnumber <= 3:
                hero2.untouched()
                print(f'Enemy health {enemy1.health}\n')
                print(f'Enemy number: {rndenemynumber}')
                if enemy1.health == 0:
                    print('Enemy defeat')
                    break
                else:
                    print('Keep attacking\n')
            else:
                print('\nMiss\n')

            #Enemy attack
            if rndenemynumber <= 5:
                hero1.health -= enemy1.smash()
                print(f'Hero health {hero1.health}\n')
            else:
                print('\nEnemy miss\n')
        elif hero1.health == 0:
            print('You died :-<')
            break
        else:
            break

stats()