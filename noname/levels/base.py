import pygame

from noname import sprites


class BaseLevel(object):
    def __init__(self, name):
        self.name = name
        self.sprites = {}
        self.resources = {}
        self.resources["sprites"] = []
        self.player = None

    def load_sprites(self):
        for sprite in self.resources["sprites"]:
            name = sprite["name"]
            self.sprites[name] = {}
            self.sprites[name]["object"] = sprites.BasicSprite(sprite)
            self.sprites[name]["sprites"] = pygame.sprite.RenderPlain((self.sprites[name]["object"]))

    def draw(self, screen):
        for sprite in self.sprites.itervalues():
            sprite["sprites"].draw(screen)
