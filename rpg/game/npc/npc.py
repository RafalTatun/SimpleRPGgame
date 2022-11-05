from dataclasses import dataclass, field
import json

# Load JSON file with npcs
with open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/npc/data.json", "r") as data_items:
    data = json.load(data_items)


# NPC class with functionality
@dataclass
class Npc():
    id: int = None
    name: str = 'Stranger'
    text: list[str] = field(default_factory=list)
    quests: dict[str] = field(default_factory=list)
    type: str = None


    @property
    def get_id(self):
        return self.id

    @get_id.setter
    def get_id(self, value):
        self.id = value
    

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, value):
        self.name = value


    @property
    def get_text(self):
        return self.text
    
    @get_text.setter
    def get_text(self, value):
        self.text = value


    @property
    def get_quest(self):
        return self.quests

    @get_quest.setter
    def get_quest(self, value):
        self.quests = value

    
    @property
    def get_type(self):
        return self.type

    @get_type.setter
    def get_type(self, value):
        self.type = value


    # def set_npc(id, name, quests, type):
    #     pass

# All NPCs
malcolm = Npc(data['Malcolm']['id'],data['Malcolm']['name'],data['Malcolm']['text'],data['Malcolm']['quests'],data['Malcolm']['type'])    
minsz = Npc(data['Minsz']['id'],data['Minsz']['name'],data['Minsz']['text'],data['Minsz']['quests'],data['Minsz']['type'])
