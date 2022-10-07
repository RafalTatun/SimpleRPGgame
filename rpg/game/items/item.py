from dataclasses import dataclass
import json


@dataclass
class Items:
    id: int = None
    name: str = None
    description: str = None
    gold: int = None
    bonus: int = None
    

    #with open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/items/data.json", "r") as data_items:
    #   data = json.load(data_items)


    # def get_item(self, id):
    #     return self.get_item(id)


    # def set_item(self, id, name, description=None, gold=0, bonus=None):
    #     return self.set_item(id, name, description, gold, bonus)


with open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/items/data.json", "r") as data_items:
    data = json.load(data_items)

print(data)