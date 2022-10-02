from dataclasses import dataclass
import json


@dataclass
class Npc:
    id: int = None
    name: str = 'Stranger'
    quests: list = []
    type: str = None


    def get_npc(self, id, name=None, quests=None, type=None):
        if id is None:
            return Npc(id=None, name=name, quests=quests, type=type)
        elif name is None:
            pass


    def set_npc(id, name, quests, type):
        pass