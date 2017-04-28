import importlib
import logging

import pygame

from noname import constants
from noname import units
from noname import hud

logger = logging.getLogger(__name__)

if not pygame.font:
    logger.warning("Warning, fonts disabled")
if not pygame.mixer:
    logger.warning("Warning, sound disabled")


class GameClient(object):
    """ The GameClient, drawing on the screen """

    def __init__(self, server_address, width=constants.DEFAULT_WIDTH,
                 height=constants.DEFAULT_HEIGHT, fps=constants.DEFAULT_FPS,):
        pygame.init()
        self.server_address = server_address
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.level = None
        self.players = []
        self.player = None
        self.clock = pygame.time.Clock()
        self.hud = hud.Hud(self)

    def update(self, event):
        self.clock.tick(self.fps)
        self.screen.fill(0)
        self.level.draw(self.screen)
        self.player.render(self.screen)
        self.hud.render()
        self.hud.handle(event)
        pygame.display.flip()

    def run(self):
        # FIXME
        # DEV SHIT REMOVE
        import time
        start = time.time()
        # DEV SHIT REMOVE

        running = True
        self.load_level(constants.DEFAULT_LEVEL)
        while running:
            for event in pygame.event.get():
                # pygame.time.wait(500)  # dev quit
                # return  # dev quit
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return

                self.update(event)

                # IMAGE FLIP ONLY?
                # elif event.type == pygame.KEYDOWN:
                #    if self.is_controls_moving(event):
                #         self.player.move(event.key)
            keys = pygame.key.get_pressed()
            if self.is_controls_moving(keys):
                self.player.move(keys)
            if (time.time() - start) >= 20:
                running = False

    def is_controls_moving(self, keys):
        if (keys[pygame.K_UP] or keys[pygame.K_DOWN] or
           keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            logger.debug("key pressed")
            return True
        else:
            return False

        # if ((event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) or
        #   (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN)):
        #    return True
        # else:
        #    return False

    def load_level(self, name):
        module_name = "noname.levels.%s" % name
        logger.debug("Loading level: %s" % module_name)
        level_module = importlib.import_module(module_name)
        self.level = level_module.Level()
        self.level.load_sprites()

    def add_player(self, x=0, y=0):
        single_player_metadata = {
            "name": "gary",
            "file": "Gary.png",
            "width": 32,
            "height": 32,
            "position": {
                "x": x,
                "y": y,
            },
        }
        player = units.Player(single_player_metadata["name"],
                              single_player_metadata)
        # FIXME
        if self.player is None:
            self.player = player
        self.players.append(player)
