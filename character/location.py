# Game map
# Symbols:
# 0 - Field, 1 - Forest, 2 - Mountain, 3 - Town1, 4 - Swamp, 5 - Dungeon, 6 - Town2, 7 - River, 8 - Bridge, 9 - Town3
#from creatingcharacter import CreateCharacter

map =   ["|--------|",
        "|00000000|",
        "|03001110|",
        "|00071615|",
        "|00077110|",
        "|40008000|",
        "|44007700|",
        "|40002222|",
        "|00020900|",
        "|--------|"]


class Game_map():
    def __init__(self, name = None, player_location = None):
        self.name = name
        self.player_location = player_location


    # def show_map():
    #     cc.update_map()
    #     for i in range(len(map)):
    #         print(map[i])


class Town1(Game_map):
    def __init__(self, name = "Wroc", player_location = 3):
        super().__init__(name, player_location)


class Town2(Game_map):
    def __init__(self, name = "Poz", player_location = 6):
        super().__init__(name, player_location)


class Town3(Game_map):
    def __init__(self, name = "Gda", player_location = 9):
        super().__init__(name, player_location)