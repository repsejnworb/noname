import pygame

from noname import sprites


class BaseLevel(object):
    def __init__(self, name):
        self.name = name
        self.sprites = {}
        self.resources = {}
        self.resources["sprites"] = []

    def load_sprites(self):
        for sprite in self.resources["sprites"]:
            print "Loading level sprite %r" % sprite
            name = sprite["name"]
            self.sprites[name] = {}
            self.sprites[name]["object"] = sprites.BasicSprite(sprite)
            self.sprites[name]["sprites"] = pygame.sprite.RenderPlain((self.sprites[name]["object"]))

    def draw(self, screen):
        print "Drawing level %s" % self.name
        for sprite in self.sprites.itervalues():
            print "Drawing level sprite %r" % sprite
            sprite["sprites"].draw(screen)
