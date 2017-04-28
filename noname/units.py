import logging

import pygame.locals

from noname import constants
from noname.sprites import BasicSprite
from noname.inventory import PlayerInventory

logger = logging.getLogger(__name__)

DIAG_CONSTANT = 0.707


class Unit(object):
    def __init__(self, name, sprite_metadata):
        self.name = name
        logger.debug("Loading sprite for %r" % sprite_metadata)
        self.sprite = BasicSprite(sprite_metadata)


class Player(Unit):

    def __init__(self, name, sprite_metadata):
        Unit.__init__(self, name, sprite_metadata)
        self.movement_speed = 5
        self.mass = 5
        self.acceleration = 0
        self.max_acceleration = 5
        self.inventory = PlayerInventory(self, constants.PLAYER_INVENTORY_SIZE)

    def move(self, keys):
        x_move = 0
        y_move = 0

        if keys[pygame.locals.K_UP]:
            y_move -= self.movement_speed
        if keys[pygame.locals.K_DOWN]:
            y_move += self.movement_speed
        if keys[pygame.locals.K_LEFT]:
            x_move -= self.movement_speed
        if keys[pygame.locals.K_RIGHT]:
            x_move += self.movement_speed

        # limit distance to self.movement_speed when moving diagonally
        if abs(x_move) and abs(y_move):
            x_move = x_move * DIAG_CONSTANT
            y_move = y_move * DIAG_CONSTANT

        self.sprite.rect.move_ip(x_move, y_move)

    def render(self, screen):
        self.sprite.draw(screen)
