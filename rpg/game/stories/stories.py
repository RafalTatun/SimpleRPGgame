# Import Stories
import json


with open("/Users/Rafal/Desktop/Git/SimpleRPGgame/rpg/game/stories/data.json", "r") as data_items:
    data = json.load(data_items)


def get_story_data():
    return data