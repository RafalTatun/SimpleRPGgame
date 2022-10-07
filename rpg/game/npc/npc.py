from dataclasses import dataclass, field
from dataclass_wizard import JSONWizard
import json


with open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/npc/data.json", "r") as data_items:
    data = json.load(data_items)

@dataclass
class Npc(JSONWizard):
    id: int = None
    name: str = 'Stranger'
    text: list[str] = field(default_factory=list)
    quests: list[str] = field(default_factory=list)
    type: str = None


    # def get_npc(self, id, name=None, quests=None, type=None):
    #     if id is None:
    #         return Npc(id=None, name=name, quests=quests, type=type)
    #     elif name is None:
    #         pass


    # def set_npc(id, name, quests, type):
    #     pass

class Malcolm(Npc):
    def __init__(self, id=data['Malcolm']['id'], name=data['Malcolm']['name'], text=data['Malcolm']['text'],quests=data['Malcolm']['quests'], type=data['Malcolm']['type']):
        super().__init__(id, name, text, quests, type)

    

print(Malcolm.name)
print(Malcolm.id)