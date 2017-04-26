import logging

import pygame

from noname import sprites

logger = logging.getLogger(__name__)


class BaseLevel(object):
    def __init__(self, name):
        self.name = name
        self.sprites = {}
        self.resources = {}
        self.resources["sprites"] = []

    def load_sprites(self):
        for sprite in self.resources["sprites"]:
            logger.debug("Loading level sprite %r" % sprite)
            name = sprite["name"]
            self.sprites[name] = {}
            self.sprites[name]["object"] = sprites.BasicSprite(sprite)
            self.sprites[name]["sprites"] = pygame.sprite.RenderPlain((self.sprites[name]["object"]))

    def draw(self, screen):
        logger.debug("Drawing level %s" % self.name)
        for sprite in self.sprites.itervalues():
            logger.debug("Drawing level sprite %r" % sprite)
            sprite["sprites"].draw(screen)
