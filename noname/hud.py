import pygame

Vector2 = pygame.math.Vector2
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Element(pygame.Rect):
    def __init__(self, position, size):
        pygame.Rect.__init__(self, position, size)
        self.position = position
        self.size = size

    def is_clicked(self, mouse_pos):
        if self.collidepoint(mouse_pos):
            return True
        else:
            return False

    def click(self):
        raise NotImplemented()

    def handle(self, event):
        raise NotImplemented()

    def render(self, screen):
        raise NotImplemented()


class ElementCollection(pygame.Rect):
    def __init__(self, position, size):
        pygame.Rect.__init__(self, position, size)
        self.position = position
        self.size = size
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def remove(self, element):
        self.elements.remove(element)

    def render(self, screen):
        for element in self.elements:
            element.render(screen)

    def handle(self, event):
        for element in self.elements:
            element.handle(event)


class InventoryQuickbarSlot(Element):
    def __init__(self, position, size):
        Element.__init__(self, position, size)
        self.color = BLUE
        self.hovered = False
        self.clicked = False

    def click(self):
        self.clicked = True
        self.color = RED

    def unclick(self):
        self.clicked = False
        self.color = BLUE

    def handle(self, event):
        if self.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_clicked(event.pos):
                    self.click()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked:
                    self.unclick()

    def render(self, screen):
        if self.hovered:
            self.color = GREEN
        else:
            self.color = BLUE
        print self.color
        pygame.draw.rect(screen, self.color, self)


class InventoryQuickbar(ElementCollection):
    def __init__(self, position, size):
        ElementCollection.__init__(self, position, size)


class Settings(object):
    def __init__(self):
        pass


class Hud(object):
    def __init__(self, game):
        self.game = game
        self.settings = Settings()
        self.components = {}
        area = self.game.screen.get_rect()
        slot_size = 50
        margin = 1
        width = (slot_size + margin) * 5
        height = slot_size
        left = area.bottomright[0] - width
        top = area.bottomright[1] - height
        inventory_quickbar = ElementCollection(Vector2(left, top),
                                               Vector2(width, height))
        self.components["inventory_quickbar"] = inventory_quickbar
        delta_position = Vector2(0, 0)
        for i in range(5):
            position = (self.components["inventory_quickbar"].position
                        + delta_position)
            slot = InventoryQuickbarSlot(position, Vector2(slot_size,
                                                           slot_size))
            self.components["inventory_quickbar"].add(slot)
            delta_position = delta_position + Vector2(slot_size + margin, 0)

    def handle(self, event):
        for component in self.components.itervalues():
            component.handle(event)

    def render(self):
        for name, component in self.components.iteritems():
            component.render(self.game.screen)
