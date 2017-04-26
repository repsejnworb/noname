import logging
import os

import pygame

logger = logging.getLogger(__name__)


def load_image(file):
    path = "noname/resources/img/"
    path += file
    path = os.path.abspath(path)
    logger.debug("Loading image: %s" % path)
    image = pygame.image.load(path)
    return image


class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, metadata):
        pygame.sprite.Sprite.__init__(self)
        self.metadata = metadata

        self.image = load_image(self.metadata["file"])
        self.rect = self.image.get_rect()

        # rescale
        width = self.metadata["width"] if self.metadata["width"] else self.rect.width
        height = self.metadata["height"] if self.metadata["height"] else self.rect.height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        if self.metadata["position"]["x"] or self.metadata["position"]["y"] != 0:
            self.rect = pygame.Rect(width, height,
                                    self.metadata["position"]["x"],
                                    self.metadata["position"]["y"])
        self.rendered = pygame.sprite.RenderPlain((self))

    def draw(self, screen):
        self.rendered.draw(screen)
