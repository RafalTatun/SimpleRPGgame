class Troll():
    def __init__(self, health=100, rage=50):
        self.health = health
        self.rage = rage

    def smash(self):
        print('Ghaarr!')
        self.damage = 40
        self.rage -= 15
        return self.damage

    def angry(self):
        print('Aaaaa!!!')
        self.rage += 5
        return self.rage