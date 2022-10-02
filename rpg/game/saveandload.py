import json
from character.create import CreateCharacter as cc

# Save game
save = {
    'id': {
        'nickname': 'Eldkar',
        'password': 'admin'
    },
    'slots': {
        'slot1': 'New hero',
        'slot2': 'New hero',
        'slot3': 'New hero'
    },
    'network': {
        'ip': '127.0.0.1',
        'port': '8080'
    }
}

with open('save_data.txt', 'w') as save_test:
    json.dump(save, save_test)


# Load game
with open('save_data.txt') as load_test:
    data = json.load(load_test)

    print(data)