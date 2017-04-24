from noname.sprites import BasicSprite


class Unit(object):
    def __init__(self, name, sprite_metadata):
        self.name = name
        self.sprite = BasicSprite(sprite_metadata)


class Player(Unit):
    def move(self):
        pass
