import importlib

import pygame

from noname import sprites
from noname import constants
from noname import units


if not pygame.font:
    print "Warning, fonts disabled"
if not pygame.mixer:
    print "Warning, sound disabled"


class Game(object):
    """ Creates the game """

    def __init__(self, width=constants.DEFAULT_WIDTH,
                 height=constants.DEFAULT_HEIGHT):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.level = None

    def start(self):
        self.load_level(constants.DEFAULT_LEVEL)
        self.load_players()
        while True:
            self.level.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                pygame.time.wait(500)  # dev quit
                return  # dev quit
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.KEYDOWN:
                    if self.is_controls_moving(event):
                        self.level.player.move(event.key)

    def is_controls_moving(self, event):
        if ((event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) or
           (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
            return True
        else:
            return False


class PlayerInput(object):
    def is_moving(self):
        pass

    def load_level(self, name):
        module_name = "noname.levels.%s" % name
        print "Loading level: %s" % module_name
        level_module = importlib.import_module(module_name)
        self.level = level_module.Level()
        self.level.load_sprites()
